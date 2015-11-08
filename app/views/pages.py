from bson import ObjectId
from flask import Blueprint

from flask import render_template, request, redirect, flash
from flask import url_for, make_response, get_flashed_messages

from flask_restful import reqparse

from flask.ext.login import current_user, login_user, logout_user

from app.service import todosService
from app.service import reminderService
from app.service import webcomicsService
from app.service import astrosService
from app.service import musicService

from app.user import User

mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return render_template('boilerplate.html')
    elif request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username', location='form')
        parser.add_argument('password', type=str, help='Password', location='form')
        args = parser.parse_args()

        u = args.get('username')
        p = args.get('password')

        user = User.get(u)
        if (user and user.password == p):
            login_user(user)
            return redirect('/')
        else:
            flash('Username or password incorrect')

    return render_template('index.html')


@mod.route('/logout')
def logout():
    logout_user()
    return redirect('/')
