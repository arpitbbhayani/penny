from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from flask.ext.restful import reqparse

from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

from bson import ObjectId

mod = Blueprint('reminder', __name__, )

@mod.route('/<id>/delete', methods=["POST"])
def deleteReminder(id):
    id = ObjectId(id)
    ret = ReminderDao(None).delete(id)
    return jsonify(response = ret)
