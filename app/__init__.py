from flask import Flask

app = Flask(__name__)

# from app import views1

from app.views import pages
from app.views import wishapi

app.register_blueprint(pages.mod)
app.register_blueprint(wishapi.mod)
