![xinhai-clpsych](https://github.com/CAS-SIAT-XinHai/XinHai-at-CLPsych2024/assets/2136700/384233ae-5117-4377-b810-c4b0ad02aa66)
# XinHai at CLPsych2024
Our code for CLPsych 2024 Shared Task Utilising LLMs: Finding supporting evidence about an individual’s suicide risk level

## Methodology
Our system integrates fine-tuned LLMs, employing Chain of Thought and one-shot learning techniques to enhance the model's ability to extract and summarize relevant evidence. For details on our methodology, refer to our model pipeline diagram. ![Model Pipeline](pipeline.jpg)


## Installation and Usage
For a comprehensive guide on deploying and utilizing the XinHai system, including specific prompts and fine-tuning tricks outlined in our research, clone this repository and consult our code. This includes:
- Example prompts used for model training and inference
- Fine-tuning techniques and optimization tricks for improved model performance

```shell
git clone https://github.com/CAS-SIAT-XinHai/XinHai-at-CLPsych2024.git
cd XinHai-at-CLPsych2024/src
```
## Citation
If you use XinHai at CLPsych2024 in your research, please cite our work using the following BibTeX entry:

```bibtex
@inproceedings{zhu-etal-2024-xinhai,
    title = "{X}in{H}ai@{CLP}sych 2024 Shared Task: Prompting Healthcare-oriented {LLM}s for Evidence Highlighting in Posts with Suicide Risk",
    author = "Zhu, Jingwei  and
      Xu, Ancheng  and
      Tan, Minghuan  and
      Yang, Min",
    editor = "Yates, Andrew  and
      Desmet, Bart  and
      Prud{'}hommeaux, Emily  and
      Zirikly, Ayah  and
      Bedrick, Steven  and
      MacAvaney, Sean  and
      Bar, Kfir  and
      Ireland, Molly  and
      Ophir, Yaakov",
    booktitle = "Proceedings of the 9th Workshop on Computational Linguistics and Clinical Psychology (CLPsych 2024)",
    month = mar,
    year = "2024",
    address = "St. Julians, Malta",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.clpsych-1.23",
    pages = "238--246",
    abstract = "In this article, we introduce a new method for analyzing and summarizing posts from r/SuicideWatch on Reddit, overcoming the limitations of current techniques in processing complex mental health discussions online. Existing methods often struggle to accurately identify and contextualize subtle expressions of mental health problems, leading to inadequate support and intervention strategies. Our approach combines the open-source Large Language Model (LLM), fine-tuned with health-oriented knowledge, to effectively process Reddit posts. We also design prompts that focus on suicide-related statements, extracting key statements, and generating concise summaries that capture the core aspects of the discussions. The preliminary results indicate that our method improves the understanding of online suicide-related posts compared to existing methodologies.",
}
```

## Acknowledgement
- The XinHai logo and banner are generated using Stable-Diffusion-XL hosted by [Qianfan](https://cloud.baidu.com/product/wenxinworkshop?track=product) from Baidu with the prompt `logo design, heart, ocean, calm, peace, clean, light blue sea, warm sky,no human, no island, psychology conseling, empathy, relaxing, meditation, circle`
- Interactive testing recommended with [LangChain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat).
- SFT powered by [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).
