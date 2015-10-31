from flask import Flask

app = Flask(__name__)

from app.views import auth
from app.views import todo
from app.views import pages
from app.views import astros
from app.views import wishapi
from app.views import reminders
from app.views import webcomics

app.register_blueprint(auth.mod, url_prefix='/auth')
app.register_blueprint(pages.mod)
app.register_blueprint(todo.mod, url_prefix='/todos')
app.register_blueprint(reminders.mod, url_prefix='/reminders')
app.register_blueprint(webcomics.mod, url_prefix='/webcomics')
app.register_blueprint(astros.mod, url_prefix='/astros')
app.register_blueprint(wishapi.mod)
