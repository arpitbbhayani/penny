from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

from app.service import reminderService

mod = Blueprint('pages', __name__, )

@mod.route('/', methods=["GET", "POST"])
def index():
    reminders = reminderService.getAllReminders()
    remindersJson = [r.jsonify() for r in reminders]
    return render_template('index.html', reminders = remindersJson)
