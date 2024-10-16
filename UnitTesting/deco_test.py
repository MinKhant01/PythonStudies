import unittest

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet('world'), 'HELLO, WORLD')

if __name__ == '__main__':
    unittest.main()