from flask import Blueprint, render_template, request, flash
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

from app.auth import requires_roles

from app.db import db
from app.models import User

mod = Blueprint('adminuser', __name__)

@mod.route('/<user_id>', methods=["GET", "POST"])
@login_required
@requires_roles('admin')
def user(user_id):
    user = User.query.get(user_id)
    if request.method == "GET":
        user = user
    elif request.method == "POST":
        user.fname = request.form.get('fname')
        user.lname = request.form.get('lname')
        user.role = request.form.get('role')
        db.session.commit()

        flash('Data saved successfully')
    return render_template('admin/user.html', user=user)
