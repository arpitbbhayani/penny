from flask import Blueprint
from flask.ext.login import login_required

mod = Blueprint('admin', __name__, )

@mod.route('/', methods=["GET"])
@login_required
def index():
    return "Welcome Admin"
