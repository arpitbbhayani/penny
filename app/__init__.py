from os.path import expanduser
from flask import Flask

from flask.ext.stormpath import StormpathManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'
app.config['STORMPATH_API_KEY_FILE'] = expanduser('~/.stormpath/apiKey.properties')
app.config['STORMPATH_APPLICATION'] = 'Penny'

app.config['STORMPATH_LOGIN_URL'] = '/signin'
app.config['STORMPATH_REGISTRATION_URL'] = '/signup'

app.config['STORMPATH_LOGIN_TEMPLATE'] = 'login.html'
app.config['STORMPATH_REGISTRATION_TEMPLATE'] = 'signup.html'


stormpath_manager = StormpathManager(app)

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
