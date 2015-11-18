import datetime
from flask import Blueprint, request, g
from flask import render_template, redirect, flash, url_for

from flask_restful import reqparse
from flask.ext.login import login_user, logout_user

from app.oauth import OAuthSignIn
from app.models import User

from app.db import db


mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET"])
def index():
    next_url = request.args.get('next') or url_for('pages.index')
    return render_template('index.html', next_url=next_url)


@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('pages.index'))


@mod.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not g.user.is_anonymous:
        return redirect(url_for('pages.index'))

    next_url = request.args.get('next') or url_for('pages.index')
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize(next_url)


@mod.route('/callback/<provider>')
def oauth_callback(provider):
    next_url = request.args.get('next') or url_for('pages.index')
    if not g.user.is_anonymous:
        return redirect(url_for('pages.index'))
    oauth = OAuthSignIn.get_provider(provider)

    print "Calling oauth callback with next_url = %s" % next_url
    social_id, fname, lname, email = oauth.callback(next_url)

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
    return redirect(next_url)
