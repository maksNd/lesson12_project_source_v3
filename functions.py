import json


def load_data_from_json(path: str) -> list[dict]:
    """Loads data from json"""
    with open(path, encoding='utf-8') as file:
        data_from_json = json.load(file)
    return data_from_json


def find_post_by_word(word: str, posts: list[dict]) -> list[dict]:
    """Finds posts by words"""
    wanted_posts = []
    for post in posts:
        if word.lower() in post.get("content").lower():
            wanted_posts.append(post)
    return wanted_posts


def add_post_to_json_file(picture_path: str, content: str, json_file: str) -> None:
    """Adds new post (picture and text) to json file"""
    with open(json_file, encoding='utf-8') as file:
        data = json.load(file)
        data.append({"pic": picture_path, "content": content})
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
