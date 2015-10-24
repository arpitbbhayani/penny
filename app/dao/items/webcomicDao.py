from pymongo import MongoClient

class WebcomicDao():

    def __init__(self):
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny


    def create_comic(self, comic_id, initial_data):
        """
        Creates a new webcomic and returns the Webcomic Object
        """
        initial_data['_id'] = comic_id
        ret = self.db.webcomics.insert_one(initial_data)
        return initial_data


    def get_comic_by_id(self, comic_id):
        """
        Returns comic object from name
        """
        ret = self.db.webcomics.find_one({
            '_id': comic_id,
            'is_active': True
        })
        return ret


    def get_all_comics_meta_info(self):
        """
        Returns list of {
            'name': '',
            'last_sync': 'time',
            'links_count': 'count'
        }
        """
        comics = []

        ret = self.db.webcomics.find({
            'is_active': True
        }, { '_id': 1, 'name': 1, 'last_sync': 1, 'links_count': 1 })

        l = []
        for comic in ret:
            id = comic.get('_id')
            name = comic.get('name')
            links_count = comic.get('links_count')

            last_sync = readable.from_ts(comic.get('last_sync')) \
                            if comic.get('last_sync') is not None else 'Never'

            comics.append({
                'id': id,
                'name': name,
                'last_sync': last_sync,
                'links_count': links_count
            })

        return comics
