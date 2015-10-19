from app.dao.todoDao import TodoDao

class Todo():

    def __init__(self, c=None, id=None):
        self.id = id
        self.content = c

    @classmethod
    def fromId(cls, id):
        ret = TodoDao(None).fromId(id)
        return cls(ret.get('content'), ret.get('_id'))

    def getId(self):
        return self.id

    def getContent(self):
        return self.content

    def setContent(self, c):
        self.content = c
