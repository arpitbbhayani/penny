from abc import ABCMeta, abstractmethod

class db:

    __metaclass__ = ABCMeta

    @abstractmethod
    def setup(self): raise NotImplementedError()


    def addConfig(self, key, value):
        raise NotImplementedError()


    def removeConfig(self, key):
        raise NotImplementedError()


    def getConfig(self, key):
        raise NotImplementedError()


    def updateConfig(self, key, value):
        raise NotImplementedError()
