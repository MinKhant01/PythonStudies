import unittest
from unittest.mock import patch

def get_data_from_api():
    return {"status": 200, "data": "real data"}

def process_data():
    data = get_data_from_api()
    if data["status"] == 200:
        return f"Processed {data["data"]}"
    else:
        return "Failed to process data"

class TestProcessData(unittest.TestCase):
    @patch('__main__.get_data_from_api')
    def test_process_data_success(self, mock_get_data):
        mock_get_data.return_value = {"status": 200, "data": "mocked data"}
        result = process_data()
        self.assertEqual(result, "Processed mocked data")
    
    @patch('__main__.get_data_from_api')
    def test_process_data_failure(self, mock_get_data):
        mock_get_data.return_value = {"status": 500, "data": "mocked data"}
        result = process_data()
        self.assertEqual(result, "Failed to process data")
    
if __name__ == "__main__":
    unittest.main()