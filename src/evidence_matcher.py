import csv
import json
from difflib import SequenceMatcher
import spacy
import re
from tqdm import tqdm
import string


# 读取CSV文件
def read_csv(file_path):
    posts = {}
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            post_id = row["post_id"]
            full_text = row["post_title"] + " " + row["post_body"]
            posts[post_id] = full_text
    return posts


# 读取JSON文件
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
    return data


nlp = spacy.load("en_core_web_lg")


def is_valid_match(candidate_match, original_text):
    # 检查是否以标点符号开头或结尾
    if (
        candidate_match[0] in string.punctuation
        or candidate_match[-1] in string.punctuation
    ):
        return False
    # 检查每个单词是否在原文中完整出现
    for word in candidate_match.split():
        if not (
            word in original_text.split()
            or word.lower() in original_text.lower().split()
        ):
            return False
    return True


def find_most_similar_words_spacy(
    original_text, target_words, max_length=5, similarity_threshold=0.3
):
    original_doc = nlp(original_text)
    target_doc = nlp(" ".join(target_words))
    best_match = None
    best_similarity = 0

    for i in range(len(original_doc)):
        for j in range(i, min(i + max_length, len(original_doc))):
            original_phrase = original_doc[i : j + 1]
            if original_phrase.has_vector and target_doc.has_vector:
                candidate_match = " ".join(token.text for token in original_phrase)
                similarity = original_phrase.similarity(target_doc)
                if similarity > best_similarity and is_valid_match(
                    candidate_match, original_text
                ):
                    best_similarity = similarity
                    best_match = candidate_match

    return best_match if best_similarity >= similarity_threshold else []


def create_regex_pattern(target_phrase):
    # 将目标短语分解为单词并为每个单词创建一个正则表达式模式
    words = target_phrase.split()
    pattern_words = [re.escape(word) for word in words]  # 使用 re.escape 避免特殊字符问题
    # 用可变长度的空白字符连接每个单词
    regex_pattern = r'\s*'.join(pattern_words)
    return regex_pattern

def find_match_with_regex(original_text, target_phrase):
    pattern = create_regex_pattern(target_phrase)
    match = re.search(pattern, original_text)
    return match.group() if match else None

def update_json_with_phrase_matches(
    csv_data, json_data, max_length=5, similarity_threshold=0.5
):
    total_posts = sum(len(item["posts"]) for item in json_data.values())
    with tqdm(total=total_posts, desc="Matching Highlights") as pbar:
        for item in json_data.values():
            for post in item["posts"]:
                post_id = post["post_id"]
                original_text = csv_data.get(post_id, "")
                highlights = post.get("highlights", [])
                if highlights is None:
                    highlights = []
                new_highlights = []
                for highlight in highlights:
                    highlight_words = highlight.split()
                    matched_phrase = find_most_similar_words_spacy(
                        original_text, highlight_words, max_length, similarity_threshold
                    )
                    if matched_phrase:
                        matched_phrase = find_match_with_regex(
                        original_text, matched_phrase
                    )
                    if matched_phrase:
                        new_highlights.append(matched_phrase)

                post["highlights"] = new_highlights
                pbar.update(1)
    return json_data


# 更新JSON数据
def find_exact_match_in_text(original_text, target_phrase):
    return target_phrase if target_phrase in original_text else None


def update_json_with_sentence_matches(csv_data, json_data):
    total_posts = sum(len(item["posts"]) for item in json_data.values())
    with tqdm(total=total_posts, desc="Matching Highlights") as pbar:
        for item in json_data.values():
            for post in item["posts"]:
                post_id = post["post_id"]
                original_text = csv_data.get(post_id, "")
                highlights = post.get("highlights", [])
                if highlights is None:
                    highlights = []
                new_highlights = []
                for highlight in highlights:
                    exact_match = find_exact_match_in_text(original_text, highlight)
                    if exact_match:
                        new_highlights.append(exact_match)
                post["highlights"] = new_highlights
                pbar.update(1)
    return json_data


# 更新后的执行流程
csv_data = read_csv("umd_reddit_suicidewatch_dataset_v2/expert/expert_posts.csv")
json_data = read_json("submission_with_summary_v4.json")
updated_json = update_json_with_sentence_matches(csv_data, json_data)

# 将更新后的JSON数据写入文件
output_file_path = "updated_submission_with_summary_v4_sentence.json"  # 可以替换为您想要的文件名
with open(output_file_path, "w", encoding="utf-8") as file:
    json.dump(updated_json, file, indent=2, ensure_ascii=False)

print(f"Updated JSON data has been saved to {output_file_path}")
