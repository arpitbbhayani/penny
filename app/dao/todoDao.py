from pymongo import MongoClient

class TodoDao():

    def __init__(self, todoObj):
        self.todoObj = todoObj
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny

    def create(self):
        ret = self.db.todo.insert_one({
            'content': self.todoObj.getContent()
        })
        return {
            'id': ret.inserted_id
        }

    def fromId(self, id):
        ret = self.db.todo.find_one({
            '_id': id
        })
        return ret

    def getTodoId(self):
        ret = self.db.todo.find_one({
            '_id': 'meta'
        })
        return ret['todoid']

    def save(self):
        ret = self.db.todo.update({'_id': self.todoObj.getId()}, { '$set': {
            'content': self.todoObj.getContent()
        }}, upsert = False)
        return {
            'id': self.todoObj.getId(),
            'updated': ret.get('updatedExisting')
        }
