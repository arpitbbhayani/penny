from app.utils import readable
from pymongo import MongoClient

class AstroDao():

    def __init__(self):
        self.client  = MongoClient('mongodb://localhost:27017/')
        self.db      = self.client.penny


    def create_astro(self, astro_id, initial_data):
        """
        Creates a new astro
        """
        initial_data['_id'] = astro_id
        ret = self.db.astros.insert_one(initial_data)
        return initial_data


    def update_astro(self, astro_id, **kwargs):
        ret = self.db.astros.update_one({
            '_id': astro_id
        }, {'$set': kwargs })
        return ret


    def add_links(self, astro_id, content):
        ret = self.db.astros.update({
            '_id': astro_id
        }, {
            '$pushAll': {
                'links': content
            }
        })

        return ret


    def get_astros_ids(self):
        """
        Returns list of astro ids
        """
        ret = self.db.astros.find({})
        return [r.get('_id') for r in ret]


    def get_astro_by_id(self, astro_id):
        """
        Returns astro object
        """
        ret = self.db.astros.find_one({
            '_id': astro_id,
            'is_active': True
        })
        return ret


    def get_astro_urls(self, astro_id):
        """
        Returns list of urls
        """
        astro = self.db.astros.find_one({
            '_id': astro_id
        },{'links.url' : 1})

        return [link.get('url') for link in astro.get('links')]


    def get_all_astros_meta_info(self):
        """
        Returns list of {
            'name': '',
            'last_sync': 'time',
            'links_count': 'count'
        }
        """
        astros = []

        ret = self.db.astros.find({
            'is_active': True
        }, { '_id': 1, 'name': 1, 'last_sync': 1, 'links_count': 1 })

        for astro in ret:
            id = astro.get('_id')
            name = astro.get('name')
            links_count = astro.get('links_count')

            last_sync = readable.from_ts(astro.get('last_sync')) \
                            if astro.get('last_sync') is not None else 'Never'

            astros.append({
                'id': id,
                'name': name,
                'last_sync': last_sync,
                'links_count': links_count
            })

        return astros
