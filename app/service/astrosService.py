import time

import app
from app.utils import readable
from app.dao.items.astroDao import AstroDao

from app.crawlers.quarks_crawler import QuarksCrawler


def create_astro(astro_id, initial_data):
    dao = AstroDao()
    astroObj = dao.create_astro(astro_id, initial_data)
    return astroObj


def get_astro(astro_id):
    dao = AstroDao()
    astro = dao.get_astro_by_id(astro_id)
    return astro


def get_astro_urls(astro_id):
    dao = AstroDao()
    urls = dao.get_astro_urls(astro_id)
    return urls


def get_astros_ids():
    dao = AstroDao()
    ids = dao.get_astros_ids()
    return ids


def sync(astro_id):
    dao, crawler = None, None

    if astro_id == 'quarks':
        dao = AstroDao()
        crawler = QuarksCrawler(app.config.QUARKS_CRAWLER_URL)
    else:
        raise Exception('Invalid astro id %s' % astro_id)

    urls = get_astro_urls(astro_id)
    astro_links = crawler.get_astros(urls)

    last_sync = time.time()
    links_count = len(astro_links) + len(urls)

    dao.add_links(astro_id, astro_links)
    dao.update_astro(astro_id, links_count=links_count, last_sync=last_sync)

    return {
        'id': astro_id,
        'links_count': links_count,
        'last_sync': readable.from_ts(last_sync)
    }


def get_astros_meta_info():
    astros = AstroDao().get_all_astros_meta_info()
    return astros
