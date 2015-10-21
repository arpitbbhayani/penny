from app.dao.todoDao import TodoDao

class Todo():

    def __init__(self, name, content):
        self.name = name
        self.content = content

    @classmethod
    def fromDB(cls, dbObj):
        obj = cls(dbObj.get('name'), dbObj.get('content'))
        obj.id = dbObj.get('_id')
        return obj

    def jsonify(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'content': self.content
        }
