from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'

# from app import views1

from app.views import todo
from app.views import pages
from app.views import astros
from app.views import music
from app.views import wishapi
from app.views import reminders
from app.views import webcomics

app.register_blueprint(pages.mod)
app.register_blueprint(todo.mod, url_prefix='/todos')
app.register_blueprint(reminders.mod, url_prefix='/reminders')
app.register_blueprint(webcomics.mod, url_prefix='/webcomics')
app.register_blueprint(astros.mod, url_prefix='/astros')
app.register_blueprint(music.mod, url_prefix='/music')
app.register_blueprint(wishapi.mod)

login_manager = LoginManager()
login_manager.init_app(app)

from app.user import User

@login_manager.user_loader
def load_user(id):
    return User.get(id)
