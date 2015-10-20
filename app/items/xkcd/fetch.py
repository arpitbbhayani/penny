from pymongo import MongoClient

def updateWhatifDB():
    client  = MongoClient('mongodb://localhost:27017/')
    db      = client.penny

    ret = db.xkcd.find({'_id': 'whatif'})
    print ret

def updateComicsDB():
    client  = MongoClient('mongodb://localhost:27017/')
    db      = client.penny

    ret = db.xkcd.find({'_id': 'comic'})
    print ret
