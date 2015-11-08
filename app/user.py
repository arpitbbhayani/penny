from flask.ext.login import UserMixin

class UserNotFoundError(Exception):
    pass

class User(UserMixin):
    USERS = {
        # username: password
        'john': 'abc',
        'mary': 'abc'
    }

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            return self_class(id)
        except UserNotFoundError:
            return None
