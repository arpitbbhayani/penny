from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

from app.auth import requires_roles

from app.models import User

mod = Blueprint('adminuser', __name__)

@mod.route('/<user_id>/edit', methods=["GET"])
@login_required
@requires_roles('admin')
def edit(user_id):
    user = User.query.get(user_id)
    return render_template('admin/user.html', user=user)
