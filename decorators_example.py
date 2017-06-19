class memoized(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):

        if

        return self.func(*args)

        if args in self.cache:
            return self.cache[args]

        else:
            result = self.func(*args)
            self.cache[args] = result
            return result
