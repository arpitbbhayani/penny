from flask import Blueprint, request, g
from flask import render_template, redirect, flash, url_for

from flask_restful import reqparse

from flask.ext.login import login_user, logout_user, login_required

mod = Blueprint('user', __name__, )


@mod.route('/')
@login_required
def activity_log():
    return "Activity Log"


@mod.route('/configure')
@login_required
def configure():
    g.user.get_preferences()
    return render_template('user/configure.html')
