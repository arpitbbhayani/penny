from flask import Blueprint

from flask import request
from flask import url_for, make_response, jsonify

mod = Blueprint('webcomics', __name__, )

@mod.route('/<id>/sync', methods=["POST"])
def deleteReminder(id):
    return jsonify(count=10)
