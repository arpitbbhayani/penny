from bson import ObjectId
from flask import Blueprint

from flask import render_template, request, redirect, flash
from flask import url_for, make_response, get_flashed_messages

from flask_restful import reqparse

from flask.ext.stormpath import login_required, user

from app.service import todosService
from app.service import reminderService
from app.service import webcomicsService
from app.service import astrosService
from app.service import musicService

mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET"])
def index():
    if user.__dict__:
        return render_template('boilerplate.html')

    return render_template('index.html')
