from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

mod = Blueprint('wishapi', __name__, )

@mod.route('/wish', methods=["GET", "POST"])
def wishapi():
    return "Wish API Hit"
