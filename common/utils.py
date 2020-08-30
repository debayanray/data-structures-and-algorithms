import functools
import time


def time_it(func):

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('"{0}" took {1} milliseconds to finish.'.format(
            func.__name__, (end_time - start_time) * 1000))
        return result

    return wrapper_func
