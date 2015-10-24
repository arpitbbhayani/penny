from flask import Blueprint

from flask import request
from flask import url_for, make_response, jsonify

from app.service import webcomicsService

mod = Blueprint('webcomics', __name__, )

@mod.route('/<comic_id>/sync', methods=["POST"])
def sync_webcomic(comic_id):
    ret = webcomicsService.sync(comic_id)
    return jsonify(resp=ret)
