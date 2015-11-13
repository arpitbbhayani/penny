import datetime
from flask import Blueprint, request

from flask import render_template, redirect, flash, get_flashed_messages, url_for
from flask_restful import reqparse

from flask.ext.login import current_user, login_user, logout_user

from app.oauth import OAuthSignIn
from app.models import User

from app.db import db


mod = Blueprint('pages', __name__, )

@mod.route('/', methods=["GET"])
def index():
    if current_user.is_authenticated:
        return render_template('boilerplate.html')
    return render_template('index.html')


@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('pages.index'))


@mod.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('pages.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@mod.route('/callback/<provider>')
def oauth_callback(provider):
    print request.values
    if not current_user.is_anonymous:
        return redirect(url_for('pages.index'))
    oauth = OAuthSignIn.get_provider(provider)

    social_id, fname, lname, email = oauth.callback()

    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('pages.index'))
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(social_id=social_id, fname=fname, lname=lname, email=email)
        db.session.add(user)
        db.session.commit()
    else:
        user.last_login = datetime.datetime.utcnow()
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('pages.index'))
