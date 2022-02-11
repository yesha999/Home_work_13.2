import json


def _load_posts():
    with open("posts.json", encoding='utf-8') as f:
        posts = json.load(f)
        if posts:
            return posts
        return []


def search_all_tags():
    all_tags = []
    posts = _load_posts()
    for post in posts:
        content = post["content"]
        for word in content.split():
            if word.startswith("#"):
                all_tags.append(word[1:])

    return all_tags


def posts_by_tag(tag):
    posts = _load_posts()
    posts_w_tag = []
    for post in posts:
        if f"#{tag}" in post["content"]:
            posts_w_tag.append(post)
    return posts_w_tag


def update_json_file(picture, content):
    """Для того чтобы подгружать ссылку на контент и картинку в жсон"""
    data = {}
    data["picture"] = picture
    data["content"] = content
    posts = _load_posts()  # Изначально хотел добавлять через with open("posts.json", "a"),
    # но словарь добавленного поста добавлялся вне списка,
    # не нашел в гугле решение по данному вопросу
    # и к сожалению или к счастью, в жсон файле теперь всё в 1 строку
    posts.append(data)
    with open("posts.json", "w", encoding='utf-8') as f:
        json.dump(posts, f)
