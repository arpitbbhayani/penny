import json
import subprocess as sub

import datetime

from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

def process(wish):
    print 'Processing wish for: %s' % (wish)
    remindDict = fetch(wish)
    print 'Dictionary :', remindDict

    remindObj = Reminder.fromDict(remindDict)

    dao = ReminderDao(remindObj)
    ret = dao.create()
    remindObj.setId(ret.get('id'))

    return remindObj.jsonify()


def fetch(wish):
    p = sub.Popen('remind', stdin = sub.PIPE, \
                        stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate(input = wish)
    print 'Output: ', output
    remindInfo = json.loads(output)

    m = remindInfo.get('message')
    t = remindInfo.get('time')
    d = remindInfo.get('date')

    if d is None:
        d = datetime.date.today()

    if t is None:
        t = datetime.time(9, 10, 0)

    if m is None:
        m = 'Reminder of something!'

    return {
        'd'     : str(d),
        't'     : str(t),
        'm'     : m
    }
