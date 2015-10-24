import random

from app.service import webcomicsService

def process(wish):
    resp, error = None, None

    webcomicDict = fetch(wish)
    comic_ids = webcomicsService.get_comics_ids()

    comic_id = webcomicDict.get('comic')

    if comic_id == 'all':
        comic_id = random.choice(comic_ids)

    if comic_id not in comic_ids:
        resp = None
        error = 'Invaid comic ID'
    else:
        urls = webcomicsService.get_comic_urls(comic_id)

        if len(urls) == 0:
            resp = None
            error = 'No comics synced yet'
        else:
            resp = random.choice(urls)

    return resp, error


def fetch(wish):
    if wish is not None:
        wish = wish.strip()

    if wish is None or len(wish) == 0:
        return {
            'comic' : 'all'
        }

    return {
        'comic': wish.split()[0]
    }
