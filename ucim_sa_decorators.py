class count_calls(object):

    # This decorator should keep track of different function calls,
    # i.e. it needs some kind of 'global' container

    global_container = dict()

    def __init__(self, func):
        self.counter = 0
        self.func = func
        count_calls.global_container[func] = self

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)

    def counter(self):
        return count_calls.global_container[self.func].counter

        @functools.wraps(self.func)
        def wrapper(*args, **kwargs):
            self.counter += 1
            result = self.func(*args, **kwargs)()
            return result
        return wrapper

    @classmethod
    def freq(c):

        d = dict()

        for funcs in c.global_container:
            d[funcs] = (funcs.__name__, c.global_container[funcs].counter)

        return d

    @classmethod
    def reset_all_counters(c):
        c.global_containers = dict()
        
