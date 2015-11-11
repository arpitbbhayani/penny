import datetime
from bson import ObjectId
from flask import Blueprint

from flask import render_template, request, redirect, flash
from flask import url_for, make_response, get_flashed_messages

from flask_restful import reqparse
from flask.ext.login import current_user, login_user, logout_user

from app.oauth import OAuthSignIn

from app.models import User

from app.db import db


mod = Blueprint('pages', __name__, )

@mod.route('/', methods=["GET"])
def index():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return render_template('boilerplate.html')
    # elif request.method == 'POST':
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('username', type=str, help='Username', location='form')
    #     parser.add_argument('password', type=str, help='Password', location='form')
    #     args = parser.parse_args()
    #
    #     u = args.get('username')
    #     p = args.get('password')
    #
    #     user = User.get(u)
    #     if (user and user.password == p):
    #         login_user(user)
    #         return redirect('/')
    #     else:
    #         flash('Username or password incorrect')

    return render_template('index.html')


@mod.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@mod.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect('/')
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@mod.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect('/')
    oauth = OAuthSignIn.get_provider(provider)

    social_id, fname, lname, email = oauth.callback()

    if social_id is None:
        flash('Authentication failed.')
        return redirect('/')
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, fname=fname, lname=lname, email=email)
        db.session.add(user)
        db.session.commit()
    else:
        user.last_login = datetime.datetime.utcnow()
        db.session.commit()
    login_user(user, True)
    return redirect('/')
