from flask import Blueprint, render_template

index_blueprint = Blueprint("index_blueprint", __name__, template_folder='templates')

@index_blueprint.route('/')
def index_page():
    return render_template('index.html')
