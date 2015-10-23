from bson import ObjectId

from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

from crontab import CronTab

def getAllReminders():
    l = [Reminder(id=r.get('_id'), m=r.get('m'),\
                    d=r.get('d'), t=r.get('t')) for r in ReminderDao(None).all()]
    return l

def delete_reminder(id):
    id = ObjectId(id)
    ret = ReminderDao(None).delete(id)

    # Delete Cron Job
    tab = CronTab(user=True)
    jobs = tab.find_comment(str(id))
    for j in jobs:
        tab.remove(j)

    #writes content to crontab
    tab.write()

    return ret
