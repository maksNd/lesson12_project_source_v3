from flask import Blueprint, render_template, request
from functions import add_post_to_json_file
from constants import POST_PATH, UPLOAD_FOLDER

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/', methods=['POST'])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.values.get("content")
    picture_path = f'uploads/images/{picture.filename}'
    picture.save(picture_path)
    add_post_to_json_file(picture_path, content, POST_PATH)
    return render_template('post_uploaded.html', picture_name=picture.filename, content=content)
