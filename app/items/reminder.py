from app.dao.reminderDao import ReminderDao

class Reminder():

    def __init__(self, id=None, m=None, t=None, d=None):
        self.id = id
        self.message = m
        self.time = t
        self.date = d

    @classmethod
    def fromId(cls, id):
        ret = ReminderDao(None).fromId(id)
        return cls(m = ret.get('m'), id = ret.get('_id'), d = ret.get('d'), t = ret.get('t'))

    @classmethod
    def fromDict(cls, remindDict):
        m = remindDict.get('m')
        d = remindDict.get('d')
        t = remindDict.get('t')
        return cls(m=m, d=d, t=t)

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getMessage(self):
        return self.message

    def setMessage(self, m):
        self.message = m

    def getTime(self):
        return self.time

    def setTime(self, t):
        self.time = t

    def getDate(self):
        return self.date

    def setDate(self, d):
        self.date = d

    def toDict(self):
        return {
            'id': self.id,
            'm' : self.message,
            't' : self.time,
            'd' : self.date
        }

    def jsonify(self):
        return {
            'id': str(self.id),
            'm' : self.message,
            't' : self.time,
            'd' : self.date
        }
