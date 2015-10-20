from app.items.reminder import Reminder
from app.dao.reminderDao import ReminderDao

def getAllReminders():
    l = [Reminder(id=r.get('_id'), m=r.get('m'),\
                    d=r.get('d'), t=r.get('t')) for r in ReminderDao(None).all()]
    return l
