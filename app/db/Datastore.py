from db import db
from pydoc import locate

from .. import config


class Datastore(db):

    _instance = None

    def __new__(classref, *args, **kwargs):
        if not classref._instance:
            classref._instance = super(Datastore, classref).\
                    __new__(classref, *args, **kwargs)

            classref._instance.db = locate('app.db.' + config.db + '.' + config.db)()
        return classref._instance


    def setup(self):
        return self.db.setup()


    def addConfig(self, key, value):
        return self.db.addConfig(key, value)


    def removeConfig(self, key):
        return self.db.removeConfig(key)


    def getConfig(self, key):
        return self.db.getConfig(key)


    def updateConfig(self, key, value):
        return self.db.updateConfig(key, value)
