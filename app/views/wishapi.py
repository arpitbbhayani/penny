from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

from ..items.remind import remind

mod = Blueprint('wishapi', __name__, )

@mod.route('/wish', methods=["GET", "POST"])
def wishapi():
    wish = request.args.get('wish')

    index = wish.index(' ')
    command = wish[:index]
    wish = wish[index+1:]

    return remind.fetch(wish)
