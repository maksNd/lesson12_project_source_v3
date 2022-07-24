from flask import Flask, send_from_directory
from bp_main.main_blueprint import index_blueprint
from bp_loader.bp_loader import loader_blueprint
from bp_search.bp_search import search_blueprint
from loggers import get_and_set_logger

get_and_set_logger()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024

app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint, url_prefix='/search')
app.register_blueprint(loader_blueprint, url_prefix='/post')


@app.route("/search/uploads/<path:path>")
def static_dir_for_bp_search(path):
    return send_from_directory("uploads", path)


@app.route("/post/uploads/<path:path>")
def static_dir_for_bp_loader(path):
    return send_from_directory("uploads", path)


@app.route("/styles/<path:path>")
def styles_dir(path):
    return send_from_directory("styles", path)


if __name__ == '__main__':
    app.run(debug=True)
