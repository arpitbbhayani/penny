from flask import Blueprint
from flask.ext.login import login_required

from app.auth import requires_roles

mod = Blueprint('admin', __name__, )

@mod.route('/', methods=["GET"])
@login_required
@requires_roles('admin')
def index():
    return "Welcome Admin"
