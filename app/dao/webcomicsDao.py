from pymongo import MongoClient

class WebcomicsDao():

    def __init__(self):
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny

    def create(self, comic):
        ret = self.db.webcomics.insert_one({
            '_id': comic
        })

    def comics(self):
        ret = self.db.webcomics.find({})
        return ret

    def getCount(self, comic):
        ret = self.db.webcomics.find({
            '_id': comic
        }, { 'contents': 1 }).count()
        return ret

    @classmethod
    def fromId(id):
        ret = self.db.webcomics.find({
            '_id': comic
        }, { 'contents': 1 }).count()
        return ret
