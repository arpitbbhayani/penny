from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

from app.service import todosService
from app.service import reminderService
from app.service import webcomicsService

mod = Blueprint('pages', __name__, )

@mod.route('/', methods=["GET", "POST"])
def index():

    # reminders
    reminders = reminderService.getAllReminders()
    remindersJson = [r.jsonify() for r in reminders]

    # todos
    todos = todosService.get_todos()

    # comics
    comics_meta = webcomicsService.get_comics_meta_info()

    return render_template('index.html', reminders=remindersJson,  comics=comics_meta, todos=todos)
