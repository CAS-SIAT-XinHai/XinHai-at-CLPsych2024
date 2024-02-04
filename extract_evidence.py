# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 13:50
# @Author  : TimLeo
# @FileName: extract_evidence.py.py
# @Software: PyCharm
import json
import csv
import requests
from tqdm import tqdm
import re


def extract_evidences(text):
    # Regular expression to match the "Extracted Evidences" list
    pattern = r'"Extracted Evidences": \[\s*([^]]+?)\s*\]'
    match = re.search(pattern, text)

    # Extract and process the matched text
    if match:
        evidences_str = match.group(1)
        # Splitting by comma and removing quotes and extra whitespaces
        evidences_list = [
            e.strip('"').strip('"').strip() for e in evidences_str.split(",")
        ]
        return evidences_list
    else:
        return None


def remove_invisible_characters(json_string):
    # 正则表达式匹配非打印字符（除了空格、制表符、换行符等）
    # 注意：\s 匹配任何空白字符，包括空格、制表符、换行符等
    # [^\S\n\r\t] 匹配任何不是空白字符、换行符、回车符或制表符的字符
    cleaned_string = re.sub(r"[\x00-\x1F\x7F-\x9F]", "", json_string)

    return cleaned_string


def fix_unterminated_strings(text):
    # 检测未闭合的双引号
    # 此正则表达式查找一个双引号后面紧跟非双引号字符或字符串结束的模式
    # 这可能表示字符串未被正确闭合
    pattern = re.compile(r"\"[^\"]*$(?!\")", re.MULTILINE)
    # 在每个匹配到的位置添加一个双引号来闭合字符串s
    return pattern.sub(lambda m: m.group() + '"', text)


def create_chat_completion(case):
    # API endpoint
    url = "http://127.0.0.1:8000/v1/chat/completions"
    system_prompt = """
    "Role: Specialized Medical Language Model for Suicide Risk Assessment in Online Posts

    Instructions for the AI:

    1. Carefully examine the provided Reddit post. Focus on identifying phrases or words that suggest suicidal ideation, distress, or related mental health issues.

    2. Employ Chain of Thought reasoning to discern and highlight specific phrases or words from the post that are indicative of the user's mental state, considering the following criteria:

        (a) Emotions: Assess the emotions expressed, ranging from sadness to unbearable psychological pain.
        (b) Cognitions: Analyze thoughts and perceptions about suicide, including frequency of suicidal thoughts, intentions to self-harm, and the presence of a plan.
        (c) Behaviour and Motivation: Examine behaviors or actions related to suicide, access to means, coping abilities, and motivations behind suicidal ideation.
        (d) Interpersonal and Social Support: Evaluate the user's social support and relationship stability.
        (e) Mental Health-related Issues: Consider any mentioned psychiatric diagnoses, history of self-harm, or suicidal attempts.
        (f) Context/Additional Risk Factors: Take into account socioeconomic, demographic factors, exposure to suicidal behavior, chronic medical conditions, etc.

    3. Based on the identified evidences, assign a suicide risk level from the options: No Risk, Low Risk, Moderate Risk, High Risk.

    4. Provide a concise summary explaining the reasoning behind the assigned risk level. This summary should elaborate on how the extracted phrases or words align with the identified criteria.

    5. Format the output in a JSON structure with fields for 'Extracted Evidences', 'Assigned Risk Level', and 'Summary'. Ensure that the 'Extracted Evidences' field comprehensively lists the specific phrases or words identified from the Reddit post.

    Example JSON Output Format:

    {
    "Extracted Evidences": ["Specific phrase or word 1", "Specific phrase or word 2", "..."\],
    "Assigned Risk Level": "An assigned risk level according to identified criteria.",
    "Summary": "A brief explanation of the evidence and the reasoning behind the assigned risk level"
    }

    Now, process the input case into the specified output format, paying special attention to the structured list output in the case."
    """
    # Request body as JSON
    json_body = {
        "model": "string",
        "messages": [{"role": "user", "content": system_prompt + case}],
        "do_sample": True,
        "temperature": 0.3,
        "top_p": 3,
        "n": 1,
        "max_tokens": 0,
        "stream": False,
    }

    # Headers
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    # Making the POST request
    response = requests.post(url, data=json.dumps(json_body), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Handle errors (e.g., connection error, timeout, etc.)
        return {"error": f"Request failed with status code {response.status_code}"}


def load_json_data(json_file_path):
    with open(json_file_path, "r") as file:
        return json.load(file)


def load_csv_to_dict(csv_file_path):
    mapping = {}
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row["post_id"]
            value = row["post_title"] + row["post_body"]
            mapping[key] = value
    return mapping


def read_user_risk_labels(csv_file):
    user_labels = {}
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row["user_id"]
            label = row["label"]
            user_labels[user_id] = label
    return user_labels


def update_highlights(json_data, post_body_mapping, user_risk_labels):
    descriptions = {
        "a": "No Risk",
        "b": "Low Risk",
        "c": "Moderate Risk",
        "d": "Severe Risk",
        "None": "None",
    }

    total_posts = sum(len(value["posts"]) for value in json_data.values())

    with tqdm(total=total_posts, desc="Processing Posts") as pbar:
        for user_id, value in json_data.items():
            user_risk = descriptions.get(user_risk_labels.get(user_id, "None"))
            for post in value["posts"]:
                post_id = post["post_id"]
                if post_id in post_body_mapping:
                    post_body = post_body_mapping[post_id]
                    success = False
                    while not success:
                        try:
                            response = create_chat_completion(post_body)
                            content = response["choices"][0]["message"]["content"]
                            evidences_list = extract_evidences(content)

                            # Check if evidences_list is empty and user risk label
                            if evidences_list or user_risk in ["No Risk", "None"]:
                                success = True
                            else:
                                print("No evidences found. Retrying...")

                        except Exception as e:
                            print(f"Error encountered: {e}. Retrying...")
                            print(content)

                    post["highlights"] = evidences_list if evidences_list else []

                # Update progress bar after each post
                pbar.update(1)


def save_json_data(json_data, output_file_path):
    with open(output_file_path, "w") as file:
        json.dump(json_data, file, indent=4)


# File paths (replace with actual paths)
json_file_path = "submission_template.json"
csv_file_path = "umd_reddit_suicidewatch_dataset_v2/expert/expert_posts.csv"
output_file_path = "submission_v4.json"

# Load the original JSON data
json_data = load_json_data(json_file_path)

# Load CSV data and create mapping
post_body_mapping = load_csv_to_dict(csv_file_path)

# Load user risk labels
user_risk_labels = read_user_risk_labels(
    "umd_reddit_suicidewatch_dataset_v2/expert/expert.csv"
)

# Update highlights in the JSON data
update_highlights(json_data, post_body_mapping, user_risk_labels)

# Save the updated JSON data
save_json_data(json_data, output_file_path)
