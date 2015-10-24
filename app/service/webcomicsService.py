import time

from app.utils import readable
from app.dao.items.webcomicDao import WebcomicDao


def create_comic(comic_id, initial_data):
    dao = WebcomicDao()
    webcomicObj = dao.create_comic(comic_id, initial_data)
    return webcomicObj


def get_comic(comic_id):
    dao = WebcomicDao()
    comic = dao.get_comic_by_id(comic_id)
    return comic


def sync(comic_id):
    links_count = 10
    last_sync = readable.from_ts(time.time())

    return {
        'id': comic_id,
        'links_count': links_count,
        'last_sync': last_sync
    }


def get_comics_meta_info():
    comics = WebcomicDao().get_all_comics_meta_info()
    return comics
