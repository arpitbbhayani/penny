from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

from app.auth import requires_roles

from app.models import User
from app.utils import readable

mod = Blueprint('admin', __name__)

@mod.route('/', methods=["GET"])
@login_required
@requires_roles('admin')
def index():
    return render_template('admin/index.html')


@mod.route('/users', methods=["GET"])
@login_required
@requires_roles('admin')
def users():
    users = [{
            'id': user.id,
            'name': user.fname + user.lname,
            'email': user.email,
            'created_at': readable.from_datetime(user.created_at),
            'last_login': readable.from_datetime(user.last_login)
        } for user in User.query.all()]
    return render_template('admin/users.html', users=users)


@mod.route('/<astro_id>/sync', methods=["POST"])
@login_required
@requires_roles('admin')
def sync_astro(astro_id):
    ret = astrosService.sync(astro_id)
    return jsonify(resp=ret)
