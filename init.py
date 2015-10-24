# Setup DB and Collections

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client  = MongoClient('mongodb://localhost:27017/')
db = client.penny

if 'todos' not in db.collection_names():
    db.create_collection(
        'todos'
    )

if 'reminders' not in db.collection_names():
    db.create_collection(
        'reminders'
    )
    db.webcomics.ensure_index("name", unique=True)

if 'webcomics' not in db.collection_names():
    db.create_collection(
        'webcomics'
    )
    db.webcomics.ensure_index("name", unique=True)


# Create Comics
from app.service import webcomicsService

# 1. xkcd
try:
    webcomic_xkcd = webcomicsService.create_comic('xkcd', {
        '_id': 'xkcd',
        'name': 'xkcd',
        'base_url': 'http://xkcd.com/',
        'last_sync': None,
        'links_count': 0,
        'is_active': True,
        'links': []
    })
except DuplicateKeyError:
    print 'xkcd comic already exists.'
