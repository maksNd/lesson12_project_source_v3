from flask import Blueprint, render_template, request
import json
from functions import add_post_to_json_file, check_extension_file
from constants import POST_PATH, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import logging

logger = logging.getLogger('basic')

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def page_post_upload():
    picture = request.files.get("picture")

    if picture.filename == '':  # если ничего не выбрано - снова вернем форму ввода
        return render_template('post_form.html')

    if not check_extension_file(picture.filename, ALLOWED_EXTENSIONS):
        logger.info(f'Попытка загрузки не изображеня. Имя файла - {picture.filename}')
        return 'Загруженный файл - не картинка'

    content = request.values.get("content")
    picture_path = f'{UPLOAD_FOLDER}/{picture.filename}'
    picture.save(picture_path)

    try:
        add_post_to_json_file(picture_path, content, POST_PATH)

    except FileNotFoundError as error:
        print(error)
        return 'Проблемы с данными на сервере :('

    except json.decoder.JSONDecodeError as error:
        print(error)
        return 'Проблемы с данными на сервере :('

    return render_template('post_uploaded.html', picture_name=picture.filename, content=content)
