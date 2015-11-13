from flask import Blueprint
from flask import render_template, jsonify

from flask.ext.restful import reqparse
from flask.ext.login import login_required

from app.service import reminderService

mod = Blueprint('reminders', __name__, )

@mod.route('/', methods=['GET'])
@login_required
def index():
    # reminders
    reminders = reminderService.getAllReminders()
    remindersJson = [r.jsonify() for r in reminders]
    return render_template('pages/reminder_widget.html', reminders=remindersJson)


@mod.route('/<id>/delete', methods=["POST"])
@login_required
def deleteReminder(id):
    ret = reminderService.delete_reminder(id)
    return jsonify(response = ret)
