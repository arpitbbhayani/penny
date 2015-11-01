from flask import Blueprint

from flask import request, render_template
from flask import url_for, make_response, jsonify

from app.service import webcomicsService

mod = Blueprint('webcomics', __name__, )

@mod.route('/', methods=["GET"])
def index():
    comics_meta = webcomicsService.get_comics_meta_info()
    return render_template('pages/webcomics_widget.html', comics=comics_meta)


@mod.route('/<comic_id>/sync', methods=["POST"])
def sync_webcomic(comic_id):
    ret = webcomicsService.sync(comic_id)
    return jsonify(resp=ret)
