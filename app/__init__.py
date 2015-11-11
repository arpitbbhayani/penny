from flask import Flask

app = Flask(__name__)

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

from flask.ext.login import LoginManager

app.config['SECRET_KEY'] = config.APP_SECRET

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': config.FACEBOOK_APP_KEY,
        'secret': config.FACEBOOK_APP_SECRET
    }
}

from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
