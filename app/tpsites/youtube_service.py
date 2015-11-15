import json
import urlparse
import requests

import app


def get_video_api_url(video_id):
    return 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=%s&key=%s' % (video_id, app.config.GOOGLE_SERVER_API_KEY)


def get_channel_api_url(channel_id):
    return 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=%s&key=%s' % (channel_id, app.config.GOOGLE_SERVER_API_KEY)


def get_playlist_api_url(playlist_id, next_page_token):
    if next_page_token:
            return 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&pageToken=%s&maxResults=50&playlistId=%s&key=%s' % (next_page_token, playlist_id, app.config.GOOGLE_SERVER_API_KEY)
    return 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=%s&key=%s' % (playlist_id, app.config.GOOGLE_SERVER_API_KEY)


def get_video_url(video_id):
    return 'https://www.youtube.com/watch?v=%s' % (video_id)


def get_channel_id(url):
    if url.find('/channel/') == -1:
        return None
    return url.split('/channel/')[1].split('/')[0]


def crawl_playlist(playlist_id):

    print 'Crawling playlist:', playlist_id

    videos = []
    next_page_token = None

    while True:

        u = get_playlist_api_url(playlist_id, next_page_token)
        r = requests.get(u)
        j = json.loads(r.text)

        for item in j['items']:
            video_id = item['snippet']['resourceId']['videoId']

            url = get_video_url(video_id)
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['default']['url']

            print 'Adding video : ', url

            videos.append({
                'url': url,
                'title': title,
                'thumbnail': thumbnail,
                'video_id': video_id
            })

            next_page_token = j.get('nextPageToken')

        if not next_page_token:
            break

    return videos


def get_videos(url):
    """
    Returns the list of videos that are present in `url`

    videos has object video of skeleton
    video = {
        'url': VIDEO_URL,
        'title': TITLE,
        'thumbnail': THUMBNAIL URL,
    }
    """
    videos = []

    query_part = urlparse.urlsplit(url).query
    query_params = dict(urlparse.parse_qsl(query_part))

    channel_id = get_channel_id(url)
    video_id = query_params.get('v')
    playlist_id = query_params.get('list')

    if channel_id:
        u = get_channel_api_url(channel_id)
        r = requests.get(u)
        j = json.loads(r.text)

        playlist_id = j['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        video_list = crawl_playlist(playlist_id)
        videos.extend(video_list)

    elif playlist_id:
        video_list = crawl_playlist(playlist_id)
        videos.extend(video_list)

    elif video_id:
        u = get_video_api_url(video_id)
        r = requests.get(u)
        j = json.loads(r.text)

        url = url
        title = j['items'][0]['snippet']['title']
        thumbnail = j['items'][0]['snippet']['thumbnails']['default']['url']

        videos.append({
            'url': url,
            'title': title,
            'thumbnail': thumbnail,
            'video_id': video_id
        })

    return videos
