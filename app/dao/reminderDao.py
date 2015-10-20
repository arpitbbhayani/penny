from pymongo import MongoClient

class ReminderDao():

    def __init__(self, reminderObj):
        self.reminderObj = reminderObj
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny

    def create(self):
        ret = self.db.reminders.insert_one({
            'm': self.reminderObj.getMessage(),
            't': self.reminderObj.getTime(),
            'd': self.reminderObj.getDate()
        })
        return {
            'id': ret.inserted_id
        }

    def fromId(self, id):
        ret = self.db.reminders.find_one({
            '_id': id
        })
        return ret

    def delete(self, id):
        ret = self.db.reminders.remove({
            '_id': id
        })
        return ret

    def all(self):
        ret = self.db.reminders.find({})
        return ret

    def delete(self, id):
        ret = self.db.reminders.remove({
            '_id': id
        })
        return ret
