import json
import csv
import requests
from tqdm import tqdm
import re

def contains_chinese(text):
    """检查文本是否包含中文字符"""
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def label_to_description(label):
    # 将label转换成文字描述
    descriptions = {
        'a': 'No Risk',
        'b': 'Low Risk',
        'c': 'Moderate Risk',
        'd': 'Severe Risk',
        'None': 'None'
    }
    return descriptions.get(label, 'Unknown')

def create_chat_completion(case):
    # API endpoint
    url = "http://127.0.0.1:8000/v1/chat/completions"
    system_prompt = (
        "Role: A medical language model specialized in suicide risk assessment from Reddit posts\n"
        "Instructions:\n"
        "1. Carefully read the provided Reddit post.\n"
        "2. Use Chain of Thought reasoning to identify and extract phrases or words that suggest suicidal ideation, distress, or related issues.\n"
        "3. Evaluate the suicide risk level based on the identified phrases or words, using detailed criteria.\n"
        "4. Assign a risk level from the following: No Risk, Low Risk, Moderate Risk, High Risk.\n"
        "5. Provide a summary explaining the extracted phrases or words and the reasoning behind the assigned risk level.\n"
        "Output Format: A JSON structure with fields for 'Summary'.\n"
        "Example JSON Output:\n"
        "{\n"
        "  \"Summary\": \"A brief explanation of the evidence and the reasoning behind the assigned risk level\"\n"
        "}"
        "Now process the input case into output format specailly notice the List output,case:"
    )
    # Request body as JSON
    json_body = {
        "model": "string",
        "messages": [
            {
                "role": "user",
                "content": system_prompt+case
            }
        ],
        "do_sample": True,
        "temperature": 0.3,
        "top_p": 3,
        "n": 1,
        "max_tokens": 0,
        "stream": False
    }
    # Headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Making the POST request
    response = requests.post(url, data=json.dumps(json_body), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Handle errors (e.g., connection error, timeout, etc.)
        return {"error": f"Request failed with status code {response.status_code}"}




def process_posts(json_file, posts_csv_file, users_csv_file, sav_file):
    # 读取JSON文件
    with open(json_file, 'r') as file:
        data = json.load(file)

    # 读取posts CSV文件到字典
    with open(posts_csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        posts_data = {row['post_id']: row for row in reader}

    # 读取users CSV文件到字典
    with open(users_csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        users_data = {row['user_id']: row for row in reader}

    # 遍历JSON数据
    total_posts = len(data.keys())
    with tqdm(total=total_posts, desc="Processing Posts") as pbar:
        for user_id, case_data in data.items():
            user_label = users_data.get(user_id, {}).get('label', 'None')
            label_description = label_to_description(user_label)

            for post in case_data['posts']:
                post_id = post['post_id']

                # 如果CSV中有匹配的post_id
                if post_id in posts_data:
                    post_info = posts_data[post_id]
                    success = False
                    # 构建字符串
                    case_input = f"Assigned Risk Level:{label_description},Post:{post_info['post_title']},{post_info['post_body']}"

                    while not success:
                        try:
                            response = create_chat_completion(case_input)
                            content = response['choices'][0]['message']['content']
                            parsed_json = json.loads(content)
                            summary = parsed_json.get('Summary')

                            # 检查摘要是否包含中文字符
                            if summary is None or contains_chinese(summary):
                                continue
                            
                            case_data['summarized_evidence'] = summary
                            # 如果解析成功，则设置success为True
                            success = True
                        except Exception as e:
                            print(f"Error encountered: {e}. Retrying...")
                            print(content)

            # 更新进度条
            pbar.update(1)

    # 将更新后的数据写回JSON文件
    with open(sav_file, 'w') as file:
        json.dump(data, file, indent=4)

process_posts('submission_v4.json','umd_reddit_suicidewatch_dataset_v2/expert/expert_posts.csv',
              'umd_reddit_suicidewatch_dataset_v2/expert/expert.csv','submission_with_summary_v4.json')