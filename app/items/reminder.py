import datetime
from app.utils import readable
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


    def toDict(self):
        return {
            'id': self.id,
            'm' : self.message,
            't' : self.time,
            'd' : self.date
        }

    def jsonify(self):
        id = str(self.id)
        m = self.message
        t = self.time if type(self.time) == str or type(self.time) == unicode else readable.time(self.time)
        d = self.date if type(self.date) == str or type(self.date) == unicode else readable.date(self.date)
        return {
            'id': id,
            'm' : m,
            't' : t,
            'd' : d
        }
