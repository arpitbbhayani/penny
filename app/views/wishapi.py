from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from app.items import commands
from app.items.remind import remind

mod = Blueprint('wishapi', __name__, )

@mod.route('/wish', methods=["GET", "POST"])
def wishapi():
    wish = request.args.get('wish')

    index = wish.index(' ')
    command = wish[:index]
    wish = wish[index+1:]

    if command == 'remind':
        resp = remind.process(wish)
        return jsonify(type='remind', response = resp)
    else:
        return jsonify(response = 'Command not fount')


@mod.route('/commands', methods=["GET", "POST"])
def help():
    return commands.getCommands()
