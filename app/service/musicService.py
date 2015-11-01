import time
import random

from app import config
from app.utils import readable
from app.dao.items.musicDao import MusicDao

from app.tpsites import youtube_service


def create_playlist(name):
    name = name.strip()
    playlist_id = name.lower().replace(' ', '-')
    initial_data = {
        'name': name,
        'updated_at': time.time(),
        'links': [],
        'links_count': 0,
        'is_active': True
    }
    dao = MusicDao()
    error, playlist_obj = dao.create_playlist(playlist_id, initial_data)
    return error, playlist_obj


def delete_playlist(playlist_id):
    """
    Deletes a Todo with id = id
    """
    dao = MusicDao()
    error, is_deleted = dao.delete_playlist(playlist_id)
    return error, is_deleted


def get_links_in_playlist(playlist_id):
    dao = MusicDao()
    urls = dao.get_link_in_playlist(playlist_id)
    return urls


def add_links_to_playlist(playlist_id, link, site):
    dao = MusicDao()

    if site == 'youtube':
        videos = youtube_service.get_videos(link)
    else:
        raise Exception('Invalid site id %s' % site)

    existing_video_urls = [link.get('url') for link in get_links_in_playlist(playlist_id)]

    links = []

    for video in videos:
        if not video.get('url') in existing_video_urls:
            links.append(video)

    last_sync = time.time()
    links_count = len(existing_video_urls) + len(links)

    dao.add_links_to_playlist(playlist_id, links)
    dao.update_playlist(playlist_id, links_count=links_count, updated_at=last_sync)

    return None, {
        'id': playlist_id,
        'links_count': links_count,
        'updated_at': readable.from_ts(last_sync)
    }


def get_playlists_meta_info():
    dao = MusicDao()
    playlists_meta = dao.get_all_playlists_meta_info()
    return playlists_meta


def get_random_link(playlist_id):
    links = get_links_in_playlist(playlist_id)
    print links
    return None, random.choice(links)
