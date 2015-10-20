from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from flask.ext.restful import reqparse

from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

from bson import ObjectId

mod = Blueprint('reminder', __name__, )

@mod.route('/', methods=["GET"])
def getAllReminders():
    l = [Reminder(id=r.get('_id'), m=r.get('m'),\
                    d=r.get('d'), t=r.get('t')) for r in ReminderDao(None).all()]

    l = [x.jsonify() for x in l]
    return jsonify(response = l)


@mod.route('/<id>/delete', methods=["POST"])
def deleteReminder(id):
    id = ObjectId(id)
    ret = ReminderDao(None).delete(id)
    return jsonify(response = ret)
