import datetime
import bson

from flask.ext.login import UserMixin
from app.db import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id          = db.Column(db.String(24), primary_key=True, default=str(bson.ObjectId()))
    social_id   = db.Column(db.String(64), nullable=False, unique=True)
    fname       = db.Column(db.String(64), nullable=False)
    lname       = db.Column(db.String(64), nullable=False)
    email       = db.Column(db.String(64), nullable=True)
    group       = db.Column(db.String(64), nullable=False, default='user')
    created_at  = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow())
    last_login  = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow())
