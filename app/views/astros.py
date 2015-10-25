from flask import Blueprint

from flask import request
from flask import url_for, make_response, jsonify

from app.service import astrosService

mod = Blueprint('astros', __name__, )

@mod.route('/<astro_id>/sync', methods=["POST"])
def sync_astro(astro_id):
    ret = astrosService.sync(astro_id)
    return jsonify(resp=ret)
