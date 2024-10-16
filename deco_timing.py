import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.5f} seconds.")
        return result
    return wrapper


@timeit
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(3)
