from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response, jsonify

from flask.ext.restful import reqparse

from app.service import reminderService

mod = Blueprint('reminder', __name__, )

@mod.route('/', methods=['GET'])
def index():
    # reminders
    reminders = reminderService.getAllReminders()
    remindersJson = [r.jsonify() for r in reminders]
    return render_template('pages/reminder_widget.html', reminders=remindersJson)


@mod.route('/<id>/delete', methods=["POST"])
def deleteReminder(id):
    ret = reminderService.delete_reminder(id)
    return jsonify(response = ret)
