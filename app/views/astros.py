from flask import Blueprint
from flask import render_template, jsonify

from flask.ext.login import login_required

from app.service import astrosService

mod = Blueprint('astros', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    astros_meta = astrosService.get_astros_meta_info()
    return render_template('pages/astro_widget.html', astros=astros_meta)


@mod.route('/<astro_id>/sync', methods=["POST"])
@login_required
def sync_astro(astro_id):
    ret = astrosService.sync(astro_id)
    return jsonify(resp=ret)
