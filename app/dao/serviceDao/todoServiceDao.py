from pymongo import MongoClient

class TodoServiceDao():

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.penny

    def get_all_todos(self):
        return self.db.todos.find({})

    def create_todo(self, todoObj):
        r = self.db.todos.insert_one({
            'name': todoObj.name,
            'content': todoObj.content
        })
        return r.inserted_id

    def delete_todo(self, todoObj):
        r = self.db.todos.remove({
            '_id': todoObj.id
        })
        return r
