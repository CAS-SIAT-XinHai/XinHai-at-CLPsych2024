from difflib import Differ
from typing import Any, Dict, Generator, List, Optional
from typing import Tuple

import gradio as gr
from gradio.blocks import Block
from gradio.components import Component  # cannot use TYPE_CHECKING here

from llmtuner.chat import ChatModel
from llmtuner.extras.misc import torch_gc
from llmtuner.hparams import GeneratingArguments
from llmtuner.webui.common import get_model_path, list_dataset, load_config
from llmtuner.webui.common import get_save_dir
from llmtuner.webui.common import save_config
from llmtuner.webui.css import CSS
from llmtuner.webui.locales import ALERTS
from llmtuner.webui.locales import LOCALES
from llmtuner.webui.manager import Manager
from llmtuner.webui.runner import Runner
from llmtuner.webui.utils import get_time


class WebChatModel(ChatModel):

    def __init__(
            self,
            manager: "Manager",
            demo_mode: Optional[bool] = False,
            lazy_init: Optional[bool] = True
    ) -> None:
        self.manager = manager
        self.demo_mode = demo_mode
        self.model = None
        self.tokenizer = None
        self.generating_args = GeneratingArguments()

        if not lazy_init:  # read arguments from command line
            super().__init__()

        if demo_mode:  # load demo_config.json if exists
            import json
            try:
                with open("demo_config.json", "r", encoding="utf-8") as f:
                    args = json.load(f)
                assert args.get("model_name_or_path", None) and args.get("template", None)
                super().__init__(args)
            except AssertionError:
                print("Please provided model name and template in `demo_config.json`.")
            except:
                print("Cannot find `demo_config.json` at current directory.")

    @property
    def loaded(self) -> bool:
        return self.model is not None

    def load_model(self, data: Dict[Component, Any]) -> Generator[str, None, None]:
        get = lambda name: data[self.manager.get_elem_by_name(name)]
        lang = get("top.lang")
        error = ""
        if self.loaded:
            error = ALERTS["err_exists"][lang]
        elif not get("top.model_name"):
            error = ALERTS["err_no_model"][lang]
        elif not get("top.model_path"):
            error = ALERTS["err_no_path"][lang]
        elif self.demo_mode:
            error = ALERTS["err_demo"][lang]

        if error:
            gr.Warning(error)
            yield error
            return

        if get("top.adapter_path"):
            adapter_name_or_path = ",".join([
                get_save_dir(get("top.model_name"), get("top.finetuning_type"), adapter)
                for adapter in get("top.adapter_path")])
        else:
            adapter_name_or_path = None

        yield ALERTS["info_loading"][lang]
        args = dict(
            model_name_or_path=get("top.model_path"),
            adapter_name_or_path=adapter_name_or_path,
            finetuning_type=get("top.finetuning_type"),
            quantization_bit=int(get("top.quantization_bit")) if get("top.quantization_bit") in ["8", "4"] else None,
            template=get("top.template"),
            flash_attn=(get("top.booster") == "flash_attn"),
            use_unsloth=(get("top.booster") == "unsloth"),
            rope_scaling=get("top.rope_scaling") if get("top.rope_scaling") in ["linear", "dynamic"] else None
        )
        super().__init__(args)

        yield ALERTS["info_loaded"][lang]

    def unload_model(self, data: Dict[Component, Any]) -> Generator[str, None, None]:
        lang = data[self.manager.get_elem_by_name("top.lang")]

        if self.demo_mode:
            gr.Warning(ALERTS["err_demo"][lang])
            yield ALERTS["err_demo"][lang]
            return

        yield ALERTS["info_unloading"][lang]
        self.model = None
        self.tokenizer = None
        torch_gc()
        yield ALERTS["info_unloaded"][lang]

    def predict(
            self,
            chatbot: List[Tuple[str, str]],
            query: str,
            history: List[Tuple[str, str]],
            system: str,
            max_new_tokens: int,
            top_p: float,
            temperature: float
    ) -> Generator[Tuple[List[Tuple[str, str]], List[Tuple[str, str]]], None, None]:
        chatbot.append([query, ""])
        response = ""
        for new_text in self.stream_chat(
                query, history, system, max_new_tokens=max_new_tokens, top_p=top_p, temperature=temperature
        ):
            response += new_text
            new_history = history + [(query, response)]
            chatbot[-1] = [query, self.postprocess(response)]
            yield chatbot, new_history, query, response

    def postprocess(self, response: str) -> str:
        blocks = response.split("```")
        for i, block in enumerate(blocks):
            if i % 2 == 0:
                blocks[i] = block.replace("<", "&lt;").replace(">", "&gt;")
        return "```".join(blocks)


class Engine:

    def __init__(self, demo_mode: Optional[bool] = False, pure_chat: Optional[bool] = False) -> None:
        self.demo_mode = demo_mode
        self.pure_chat = pure_chat
        self.manager = Manager()
        self.runner = Runner(self.manager, demo_mode=demo_mode)
        self.chatter = WebChatModel(manager=self.manager, demo_mode=demo_mode, lazy_init=(not pure_chat))

    def _form_dict(self, resume_dict: Dict[str, Dict[str, Any]]):
        return {self.manager.get_elem_by_name(k): gr.update(**v) for k, v in resume_dict.items()}

    def resume(self) -> Generator[Dict[Component, Dict[str, Any]], None, None]:
        user_config = load_config() if not self.demo_mode else {}
        lang = user_config.get("lang", None) or "en"

        init_dict = {
            "top.lang": {"value": lang},
            "infer.chat_box": {"visible": self.chatter.loaded}
        }

        if not self.pure_chat:
            init_dict["train.dataset"] = {"choices": list_dataset()["choices"]}
            init_dict["eval.dataset"] = {"choices": list_dataset()["choices"]}

            if user_config.get("last_model", None):
                init_dict["top.model_name"] = {"value": user_config["last_model"]}
                init_dict["top.model_path"] = {"value": get_model_path(user_config["last_model"])}

        yield self._form_dict(init_dict)

        if not self.pure_chat:
            if self.runner.alive:
                yield {elem: gr.update(value=value) for elem, value in self.runner.running_data.items()}
                if self.runner.do_train:
                    yield self._form_dict({"train.resume_btn": {"value": True}})
                else:
                    yield self._form_dict({"eval.resume_btn": {"value": True}})
            else:
                yield self._form_dict({
                    "train.output_dir": {"value": "train_" + get_time()},
                    "eval.output_dir": {"value": "eval_" + get_time()},
                })

    def change_lang(self, lang: str) -> Dict[Component, Dict[str, Any]]:
        return {
            component: gr.update(**LOCALES[name][lang])
            for elems in self.manager.all_elems.values() for name, component in elems.items() if name in LOCALES
        }


def create_chat_box(
        engine: "Engine",
        visible: Optional[bool] = False
) -> Tuple["Block", "Component", "Component", Dict[str, "Component"]]:
    with gr.Box(visible=visible) as chat_box:
        chatbot = gr.Chatbot()
        history = gr.State([])
        with gr.Row():
            with gr.Column(scale=4):
                system = gr.Textbox(show_label=False)
                query = gr.Textbox(show_label=False, lines=8)
                submit_btn = gr.Button(variant="primary")

            with gr.Column(scale=1):
                clear_btn = gr.Button()
                gen_kwargs = engine.chatter.generating_args
                max_new_tokens = gr.Slider(10, 2048, value=gen_kwargs.max_new_tokens, step=1)
                top_p = gr.Slider(0.01, 1, value=gen_kwargs.top_p, step=0.01)
                temperature = gr.Slider(0.01, 1.5, value=gen_kwargs.temperature, step=0.01)

    with gr.Box(visible=visible) as diff_box:
        with gr.Row():
            original = gr.Textbox(
                label="Text 1",
                info="Initial text",
                lines=3,
                value="The quick brown fox jumped over the lazy dogs.",
            )
            prompted = gr.Textbox(
                label="Text 2",
                info="Text to compare",
                lines=3,
                value="The fast brown fox jumps over lazy dogs.",
            )

    submit_btn.click(
        engine.chatter.predict,
        [chatbot, query, history, system, max_new_tokens, top_p, temperature],
        [chatbot, history, original, prompted],
        show_progress=True
    ).then(
        lambda: gr.update(value=""), outputs=[query]
    ).then(
        diff_texts,
        [
            original,
            prompted,
        ],
        gr.HighlightedText(
            label="Diff",
            combine_adjacent=True,
            show_legend=True,
            color_map={"+": "red", "-": "green"}),
        # theme=gr.themes.Base()
    )

    clear_btn.click(lambda: ([], []), outputs=[chatbot, history], show_progress=True)

    return chat_box, chatbot, history, dict(
        system=system,
        query=query,
        submit_btn=submit_btn,
        clear_btn=clear_btn,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        temperature=temperature
    )


def diff_texts(text1, text2):
    d = Differ()
    return [
        (token[2:], token[0] if token[0] != " " else None)
        for token in d.compare(text1, text2)
    ]


def create_web_demo() -> gr.Blocks:
    engine = Engine(pure_chat=True)

    with gr.Blocks(title="Web Demo", css=CSS) as demo:
        lang = gr.Dropdown(choices=["en", "zh"])
        engine.manager.all_elems["top"] = dict(lang=lang)

        chat_box, _, _, chat_elems = create_chat_box(engine, visible=True)
        engine.manager.all_elems["infer"] = dict(chat_box=chat_box, **chat_elems)

        demo.load(engine.resume, outputs=engine.manager.list_elems())
        lang.change(engine.change_lang, [lang], engine.manager.list_elems(), queue=False)
        lang.input(save_config, inputs=[lang], queue=False)

    return demo


def main():
    demo = create_web_demo()
    demo.queue()
    demo.launch(server_name="0.0.0.0", share=False, inbrowser=True)


if __name__ == "__main__":
    main()
