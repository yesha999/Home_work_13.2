import os.path

from flask import Flask, redirect, render_template, request, send_from_directory

from functions import posts_by_tag, search_all_tags,  update_json_file

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    all_tags = search_all_tags()
    return render_template("index.html", tags=all_tags)


@app.route("/tag")
def page_tag():
    tag = request.args.get("tag")
    posts_w_tag = posts_by_tag(tag)

    return render_template("post_by_tag.html", posts=posts_w_tag, tag=tag)


@app.route("/post", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@app.route("/post", methods=["POST"])
def page_post_create():
    picture = request.files.get("picture")
    content = request.values.get("content")
    if picture:
        file_name = picture.filename
        path = os.path.join(UPLOAD_FOLDER, file_name)
        picture.save(path)
        picture_new_url = f"/{UPLOAD_FOLDER}/{file_name}"
        update_json_file(picture_new_url, content)
        return render_template("/post_uploaded.html", picture=picture_new_url, content=content)
    return redirect("/post")


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
