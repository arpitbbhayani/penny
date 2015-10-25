import random

from app.service import astrosService

def process(wish):
    resp, error = None, None

    astroDict = fetch(wish)
    astro_ids = astrosService.get_astros_ids()

    astro_id = astroDict.get('astro')

    if astro_id == 'all':
        astro_id = random.choice(astro_ids)

    if astro_id not in astro_ids:
        resp = None
        error = 'Invaid astro ID'
    else:
        urls = astrosService.get_astro_urls(astro_id)

        if len(urls) == 0:
            resp = None
            error = 'No astros synced yet'
        else:
            resp = random.choice(urls)

    return resp, error


def fetch(wish):
    if wish is not None:
        wish = wish.strip()

    if wish is None or len(wish) == 0:
        return {
            'astro' : 'all'
        }

    return {
        'astro': wish.split()[0]
    }
