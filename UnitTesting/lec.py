import unittest
from unittest.mock import Mock
from unittest.mock import patch

def divide(a, b):
    return a / b

class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1,0)

def parse_int(s):
    return int(s)

class TestParseInt(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_int('abc')

class TestExample(unittest.TestCase):
    def setUp(self):
        self.file = open('test.txt', 'w')
    
    def tearDown(self):
        self.file.close()
    
    def test_write(self):
        self.file.write("Hello")
        self.file.flush()

def get_data(api):
    return api.dudu()

class TestGetData(unittest.TestCase):
    def test_get_data(self):
        api_mock = Mock()
        api_mock.dudu.return_value = {'data': '123'}
        result = get_data(api_mock)
        self.assertEqual(result, {'data': '123'})

@patch('module.function_to_mock')
def test_function(self, mock_function):
    mock_function.return_value = "mocked!"
    result = module.function_to_test()
    self.assertEqual(result, 'expected result')