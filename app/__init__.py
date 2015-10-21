from flask import Flask

app = Flask(__name__)

# from app import views1

from app.views import todo
from app.views import pages
from app.views import wishapi
from app.views import reminders
from app.views import webcomics

app.register_blueprint(pages.mod)
app.register_blueprint(todo.mod, url_prefix='/todos')
app.register_blueprint(reminders.mod, url_prefix='/reminders')
app.register_blueprint(webcomics.mod, url_prefix='/webcomics')
app.register_blueprint(wishapi.mod)
