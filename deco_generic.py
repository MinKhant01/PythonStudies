import functools, time

def log_func_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called.")
        return func(*args, **kwargs)
    return wrapper
"""
@log_func_call
def add(a, b):
    return a + b

print(add(2,3))
print(add.__name__)
print(add.__doc__)
print(add.__module__)
"""

# decorator for a class's instance methods must accept self as first argument
def method_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print("Decorator applied to method")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @method_decorator
    def method(self):
        print("Method called.")

"""
obj = MyClass()
obj.method()
"""

# decorator class must implement __call__ method
class DecoratorClass:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result
    
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)
    
class TimeLogger:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{self.func.__name__}' took {elapsed_time} seconds to run.")
        return result

@TimeLogger
def say_hello():
    print("Hello!")

say_hello()





    
