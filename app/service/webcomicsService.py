import time

from app import config
from app.utils import readable
from app.dao.items.webcomicDao import WebcomicDao

from app.crawlers.xkcd_crawler import XkcdComic


def create_comic(comic_id, initial_data):
    dao = WebcomicDao()
    webcomicObj = dao.create_comic(comic_id, initial_data)
    return webcomicObj


def get_comic(comic_id):
    dao = WebcomicDao()
    comic = dao.get_comic_by_id(comic_id)
    return comic


def get_comic_urls(comic_id):
    dao = WebcomicDao()
    urls = dao.get_comic_urls(comic_id)
    return urls


def get_comics_ids():
    dao = WebcomicDao()
    ids = dao.get_comics_ids()
    return ids


def sync(comic_id):
    dao, crawler = None, None

    if comic_id == 'xkcd':
        dao = WebcomicDao()
        crawler = XkcdComic(config.XKCD_CRAWLER_URL)
    else:
        raise Exception('Invalid webcomic id %s' % comic_id)

    urls = get_comic_urls(comic_id)
    comic_links = crawler.get_comics(urls)

    last_sync = time.time()
    links_count = len(comic_links) + len(urls)

    dao.add_links(comic_id, comic_links)
    dao.update_comic(comic_id, links_count=links_count, last_sync=last_sync)

    return {
        'id': comic_id,
        'links_count': links_count,
        'last_sync': readable.from_ts(last_sync)
    }


def get_comics_meta_info():
    comics = WebcomicDao().get_all_comics_meta_info()
    return comics
