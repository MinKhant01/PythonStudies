def decorator_one(func):
    print("enters 1")
    def wrapper(*args, **kwargs):
        print("Decorator 1 wrapper STARTS")
        result = func(*args, **kwargs)
        print("Decorator 1 wrapper ENDS")
        return result
    print("exits 1")
    return wrapper

def decorator_two(func):
    print("enters 2")
    def wrapper(*args, **kwargs):
        print("Decorator 2 wrapper STARTS")
        result = func(*args, **kwargs)
        print("Decorator 2 wrapper ENDS")
        return result
    print("exits 2")
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()

# try it with three decorators