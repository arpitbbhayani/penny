from flask import Blueprint
from flask import render_template, jsonify

from flask.ext.login import login_required

from app.service import webcomicsService

mod = Blueprint('webcomics', __name__, )

@mod.route('/', methods=["GET"])
@login_required
def index():
    comics_meta = webcomicsService.get_comics_meta_info()
    return render_template('pages/webcomics_widget.html', comics=comics_meta)


@mod.route('/<comic_id>/sync', methods=["POST"])
@login_required
def sync_webcomic(comic_id):
    ret = webcomicsService.sync(comic_id)
    return jsonify(resp=ret)
