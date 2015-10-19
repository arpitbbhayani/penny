import json
import subprocess as sub

import datetime

def fetch(wish):
    p = sub.Popen('remind', stdin = sub.PIPE, \
                        stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate(input = wish)
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
        'str'   : 'Reminder set',
        'd'     : str(d),
        't'     : str(t),
        'm'     : m
    }
