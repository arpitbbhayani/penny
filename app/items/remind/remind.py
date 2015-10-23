import re
import json
import subprocess as sub

import datetime

from crontab import CronTab

from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

from app import config

EVERYDAY_RE = "every\s*day"
DATE_RE = "([0-9]+)[-.:/]([0-9]+)([-.:/]([0-9]+))?"
TIME_RE = "([0-9]+)\s*([:.]\s*([0-9]+))?\s*([aApP][mM])?"

def process(wish):
    resp, error = None, None

    remindDict = fetch(wish)
    message, remind_time, remind_date = extract(remindDict)

    remindObj = Reminder.fromDict({
        'm': message,
        't': remind_time,
        'd': remind_date
    })
    try:
        cron_str = get_cron_str(remindObj)
    except Exception, err:
        resp, error = None, err
        return resp, error

    dao = ReminderDao(remindObj)
    ret = dao.create()
    remindObj.id = ret.get('id')

    tab = CronTab(user=True)
    job = tab.new(config.REMIND_COMMAND, comment=str(remindObj.id))
    job.setall(cron_str)
    tab.write()

    resp = remindObj.jsonify()

    # print tab.render()
    return resp, error


def extract(remindDict):
    message, remind_time, remind_date = None, None, None

    message = remindDict.get('m')

    date = remindDict.get('d')

    matches = re.match(EVERYDAY_RE, date)

    if matches :
        remind_date = 'Everyday'

    matches = re.match(DATE_RE, date)
    if matches :
        dd = int(matches.group(1))
        mm = int(matches.group(2))

        if mm > 12:
            dd, mm = mm, dd

        remind_date = datetime.date(datetime.datetime.now().year, mm, dd)

    time = remindDict.get('t')

    matches = re.match(TIME_RE, time)

    hour = int(matches.group(1))
    minutes = int(matches.group(3)) if len(matches.groups()) >= 3 and matches.group(3) else 0
    ampm = matches.group(4) if len(matches.groups()) >= 4 else None

    if ampm and ampm.lower() == 'pm':
        hour = int(str(hour + 12))

    try:
        remind_time = datetime.time(hour, minutes)
    except:
        remind_time = None

    if remind_time is None:
        raise Exception('Invalid date %s' % time)

    if remind_date is None:
        raise Exception('Invalid date %s' % date)

    return message, remind_time, remind_date


def get_cron_str(remindObj):
    minutes, hour, day, month, weekday = '*', '*', '*', '*', '*'

    date = remindObj.date.lower() if type(remindObj.date) == str else remindObj.date.strftime('%d-%m')
    matches = re.match(EVERYDAY_RE, date)
    if matches is None:
        day = str(remindObj.date.day)
        month = str(remindObj.date.month)
        weekday = '*'

    cron_str = '%s %s %s %s %s' % (str(remindObj.time.minute),
                                str(remindObj.time.hour), day, month, weekday)

    return cron_str


def fetch(wish):
    p = sub.Popen('remind', stdin = sub.PIPE, \
                        stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate(input = wish)

    remindInfo = json.loads(output)

    m = remindInfo.get('message')
    t = remindInfo.get('time')
    d = remindInfo.get('date')

    if d is None:
        d = datetime.date.today().strftime('%d-%m-%Y')

    if t is None:
        t = str(datetime.time(9, 15))

    if m is None:
        m = 'Reminder of something!'

    return {
        'd'     : d,
        't'     : t,
        'm'     : m
    }
