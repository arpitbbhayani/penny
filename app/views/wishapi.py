from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from app.items import commands
from app.items.astro import astro
from app.items.remind import remind
from app.items.webcomic import webcomic

mod = Blueprint('wishapi', __name__, )

@mod.route('/wish', methods=["GET", "POST"])
def wishapi():
    wish = request.args.get('wish')

    index = wish.find(' ')

    if index != -1:
        command = wish[:index]
        wish = wish[index+1:]
    else:
        command = wish.strip()
        wish = None

    if command == 'remind':
        resp, error = remind.process(wish)
        if resp is None:
            resp = ''
        return jsonify(type='remind', response=resp, error=error)
    elif command == 'comic':
        resp, error = webcomic.process(wish)
        if resp is None:
            resp = ''
        return jsonify(type='comic', response=resp, error=error)
    elif command == 'astro':
        resp, error = astro.process(wish)
        if resp is None:
            resp = ''
        return jsonify(type='astro', response=resp, error=error)
    else:
        return jsonify(response = 'Command not fount')


@mod.route('/commands', methods=["GET", "POST"])
def help():
    return commands.getCommands()
