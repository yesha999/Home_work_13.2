import json


def _load_posts():
    """Загружаем посты из жсон"""
    with open("posts.json", encoding='utf-8') as f:
        posts = json.load(f)
        if posts:
            return posts
        return []


def search_all_tags():
    """Создаем список всех тегов из описаний постов"""
    all_tags = []
    posts = _load_posts()
    for post in posts:
        content = post["content"]
        for word in content.split():
            if word.startswith("#"):
                all_tags.append(word[1:])
    all_tags_no_duplicates = []
    for i in all_tags:
        if i not in all_tags_no_duplicates:
            all_tags_no_duplicates.append(i)
    return all_tags_no_duplicates


def posts_by_tag(tag):
    """Создаем список всех постов с нужным тегом"""
    posts = _load_posts()
    posts_w_tag = []
    for post in posts:
        if f"#{tag}" in post["content"]:
            posts_w_tag.append(post)
    return posts_w_tag


def update_json_file(picture, content):
    """Для того чтобы подгружать ссылку на контент и картинку в жсон"""
    data = {}
    data["pic"] = picture
    data["content"] = content
    posts = _load_posts()
    posts.append(data)
    with open("posts.json", "w", encoding='utf-8') as f:
        json.dump(posts, f)
