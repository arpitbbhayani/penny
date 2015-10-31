from app.utils import readable
from pymongo import MongoClient
from pymongo import errors

class MusicDao():

    def __init__(self):
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny


    def create_playlist(self, playlist_id, initial_data):
        """
        Creates a new playlist
        """
        initial_data['_id'] = playlist_id

        try:
            ret = self.db.music.insert_one(initial_data)
        except errors.DuplicateKeyError, e:
            return 'Playlist "%s", already exists' % initial_data.get('name'), None

        initial_data['id'] = playlist_id
        initial_data['updated_at'] = readable.from_ts(initial_data['updated_at'])
        return None, initial_data


    def delete_playlist(self, playlist_id):
        """
        Deletes a playlist
        """
        try:
            ret = self.db.music.remove({
                '_id': playlist_id
            })
        except Exception, e:
            return 'Exception in delete_playlist', None
        return None, ret is not None


    def update_playlist(self, playlist_id, **kwargs):
        ret = self.db.music.update_one({
            '_id': playlist_id
        }, {'$set': kwargs })
        return ret


    def get_urls_in_playlist(self, playlist_id):
        """
        Returns list of urls
        """
        playlist = self.db.music.find_one({
            '_id': playlist_id
        },{'links.url' : 1})

        return [link.get('url') for link in playlist.get('links')]


    def add_links_to_playlist(self, playlist_id, links):
        ret = self.db.music.update({
            '_id': playlist_id
        }, {
            '$pushAll': {
                'links': links
            }
        })
        return ret


    def get_playlist_by_id(self, playlist_id):
        """
        Returns playlist object
        """
        ret = self.db.music.find_one({
            '_id': playlist_id,
            'is_active': True
        })
        return ret


    def get_all_playlists_meta_info(self):
        """
        Returns list of {
            'name': '',
            'updated_at': 'time',
            'links_count': 'count'
        }
        """
        playlists = []

        ret = self.db.music.find({
            'is_active': True
        }, { '_id': 1, 'name': 1, 'updated_at': 1, 'links_count': 1 })

        for playlist in ret:
            id = playlist.get('_id')
            name = playlist.get('name')
            links_count = playlist.get('links_count')

            updated_at = readable.from_ts(playlist.get('updated_at')) \
                            if playlist.get('updated_at') is not None else 'Never'

            playlists.append({
                'id': id,
                'name': name,
                'updated_at': updated_at,
                'links_count': links_count
            })

        return playlists
