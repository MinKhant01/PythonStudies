def logging(func):
    def wrapper(*args, **kwargs):
        print("Logging: ", func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper

@logging
def greet():
    print("Hello!")

greet()