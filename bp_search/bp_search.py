from flask import Blueprint, render_template, request
from functions import load_data_from_json, find_post_by_word
from constants import POST_PATH

search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')


@search_blueprint.get("/")
def search_by_word():
    word_for_search = request.values.get('s')
    posts = load_data_from_json(POST_PATH)
    wanted_posts = find_post_by_word(word_for_search, posts)
    return render_template('post_list.html', s=word_for_search, wanted_posts=wanted_posts)
