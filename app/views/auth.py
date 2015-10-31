from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

from app.service import authsService

mod = Blueprint('auth', __name__, )

@mod.route('/google', methods=["GET"])
def google():
    print "ARGS : ", request.args

    if request.args.get('code'):
        credentials = authsService.authenticate_youtube(code = request.args.get('code'))
        return request.args.get('code')
    else:
        auth_uri = authsService.authenticate_youtube()
        return redirect(auth_uri)
