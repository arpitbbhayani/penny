from flask import Blueprint

from flask import request, render_template
from flask import url_for, make_response, jsonify

from app.service import astrosService

mod = Blueprint('astros', __name__, )


@mod.route('/', methods=["GET"])
def index():
    astros_meta = astrosService.get_astros_meta_info()
    return render_template('pages/astro_widget.html', astros=astros_meta)


@mod.route('/<astro_id>/sync', methods=["POST"])
def sync_astro(astro_id):
    ret = astrosService.sync(astro_id)
    return jsonify(resp=ret)
