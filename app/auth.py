from functools import wraps
from flask.ext.login import current_user

def get_current_user_role():
    return current_user.group

def error_response():
    return 'You are not admin', 401

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)
        return wrapped
    return wrapper
