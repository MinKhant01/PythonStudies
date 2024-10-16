#caching
def cached(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cached
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)