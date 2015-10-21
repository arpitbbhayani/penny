from app.dao.webcomicsDao import WebcomicsDao

def getComics():
    cursor = WebcomicsDao().comics()
    comics = [c for c in cursor]
    return comics

def getCounts():
    comics = getComics()
    d = {}
    for comic in comics:
        d[comic.id] = len(comic.contents)
    return d

def getComic(id):
    comicObj = WebcomicsDao.fromId(id)
    print comicObj
    return comicObj
