from flask import Blueprint, render_template, request, redirect
import json
from functions import add_post_to_json_file, check_extension_file
from constants import POST_PATH, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import logging

logger = logging.getLogger('basic')

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.errorhandler(413)
def page_not_found(error):
    logger.error('Попытка загрузить слишком большое изображение')
    message = "Вы пытаетесь загрузить слишком большое изображение"
    return render_template('post_not_uploaded.html', message=message)


@loader_blueprint.route('/post_form')
def page_post_form():
    return render_template('post_form.html')


# TODO добавить если запрос - GET, то ...; если запрос - POST, то ...

@loader_blueprint.route('/post', methods=['POST'])
def page_post_upload():
    picture = request.files.get("picture")

    if not picture: # если картинка для загрузки не выбрана
        return redirect('/post_form')

    if not check_extension_file(picture.filename, ALLOWED_EXTENSIONS):
        logger.info(f'Попытка загрузки не изображеня. Имя файла - {picture.filename}')
        message = 'Загружаемый файл не является изображением'
        return render_template('post_not_uploaded.html', message=message)

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
