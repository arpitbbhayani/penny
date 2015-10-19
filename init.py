from pymongo import MongoClient

from app.items.todo import Todo
from app.dao.todoDao import TodoDao

# Create a todo
client  = MongoClient('mongodb://localhost:27017/')
db      = client.penny

db.todo.insert_one({'_id': 'meta'})

dao = TodoDao(Todo(''))
ret = dao.create()
assert ret.get('id') is not None

db.todo.update({'_id': 'meta'}, {'$set' : {'todoid' : ret.get('id')}})
