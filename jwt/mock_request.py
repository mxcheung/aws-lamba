import unittest
from unittest.mock import patch
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}
        
        result = fetch_data("http://example.com/api")
        
        self.assertEqual(result, {"key": "value"})

    @patch('requests.get')
    def test_fetch_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        
        result = fetch_data("http://example.com/api")
        
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
