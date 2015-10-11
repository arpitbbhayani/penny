from pymongo import MongoClient
from bson.objectid import ObjectId

from db import db

class mongo(db):


    def __init__(self):
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.wit52


    def toId(self, id):
        """
        Returns ID of type required by database from string
        """
        return ObjectId(id)


    def setup(self):
        if 'config' not in self.db.collection_names():
            self.db.create_collection('config')


    def addConfig(self, key, value):
        """
        Adds key, value to config db
        """
        self.config.insert_one({'_id':key, 'value': value})


    def removeConfig(self, key):
        """
        Removes key from config db
        """
        self.config.delete_one({'_id':key})


    def getConfig(self, key):
        """
        Returns value for key from config db

        :return: value for key
        """
        r = self.config.find_one({'_id':key})
        if r:
            return r['value']
        return None


    def updateConfig(self, key, value):
        self.config.update_one(
            {'_id': key}, {"$set" : {'value': value}}
        )
