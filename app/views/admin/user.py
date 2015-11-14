from flask import Blueprint, render_template, request, flash, abort, redirect
from jinja2 import TemplateNotFound
from flask.ext.login import login_required

from app.auth import requires_roles

from app.db import db
from app.models import User

mod = Blueprint('adminuser', __name__)

@mod.route('/<user_id>', methods=["GET"])
@login_required
@requires_roles('admin')
def user(user_id):
    user = User.query.get(user_id)
    return render_template('admin/user.html', user=user)


@mod.route('/<user_id>/save', methods=["POST"])
@login_required
@requires_roles('admin')
def update(user_id):
    user = User.query.get(user_id)
    if request.args.get('update') == 'details':
        user.fname = request.form.get('fname')
        user.lname = request.form.get('lname')
        user.role = request.form.get('role')
        db.session.commit()
        flash('User details updated')
    elif request.args.get('update') == 'services':
        flash('Services updated')
    else:
        flash('Invalid action')
    return redirect(request.referrer)
