from flask import Blueprint

from flask import render_template, request, redirect
from flask import url_for, make_response

from app.service import todosService
from app.service import reminderService
from app.service import webcomicsService
from app.service import astrosService
from app.service import musicService

mod = Blueprint('pages', __name__, )

@mod.route('/', methods=["GET", "POST"])
def index():

    print "INDEX HIT"

    # reminders
    reminders = reminderService.getAllReminders()
    remindersJson = [r.jsonify() for r in reminders]

    # todos
    todos = todosService.get_todos()

    # comics
    comics_meta = webcomicsService.get_comics_meta_info()

    # astros
    astros_meta = astrosService.get_astros_meta_info()

    # Playlists
    playlists_meta = musicService.get_playlists_meta_info()

    return render_template('index.html', reminders=remindersJson,  \
                    comics=comics_meta, todos=todos, astros=astros_meta, \
                    playlists=playlists_meta )
