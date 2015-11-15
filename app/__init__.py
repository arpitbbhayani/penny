from flask import Flask

app = Flask(__name__)
app.config.from_object('app.config')

from app.views.user import pages, todo, reminders, webcomics, astros, music, wishapi
from app.views.admin import admin, user as adminuser

from app.views.user import user

app.register_blueprint(pages.mod)
app.register_blueprint(todo.mod, url_prefix='/todos')
app.register_blueprint(reminders.mod, url_prefix='/reminders')
app.register_blueprint(webcomics.mod, url_prefix='/webcomics')
app.register_blueprint(astros.mod, url_prefix='/astros')
app.register_blueprint(music.mod, url_prefix='/music')
app.register_blueprint(wishapi.mod)


# User Blueprints
app.register_blueprint(user.mod, url_prefix='/user')

# Admin Blueprints
app.register_blueprint(admin.mod, url_prefix='/admin')
app.register_blueprint(adminuser.mod, url_prefix='/admin/user')

from flask.ext.login import LoginManager


from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = '/'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
