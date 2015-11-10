from flask.ext.login import UserMixin
from app.db import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)


# Create tables.
db.create_all()
