from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

from app.auth import requires_roles

mod = Blueprint('admin', __name__)

@mod.route('/', methods=["GET"])
@login_required
@requires_roles('user')
def index():
    return render_template('admin/index.html')


@mod.route('/<astro_id>/sync', methods=["POST"])
@login_required
@requires_roles('user')
def sync_astro(astro_id):
    ret = astrosService.sync(astro_id)
    return jsonify(resp=ret)
