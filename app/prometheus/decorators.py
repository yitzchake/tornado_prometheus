from functools import wraps


def audit(f):
    @wraps(f)
    def wrapper(self):
        print('In wraper!')
        f(self, request)
    return wrapper
