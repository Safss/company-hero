import unittest
from unittest.mock import patch, Mock
from handler import handler

class TestHandler(unittest.TestCase):

    @patch('dependencies.get_weather_repository')
    def test_handler_success(self, mock_get_weather_repository):
        # Setup mock
        mock_repository = Mock()
        mock_use_case = Mock()
        mock_use_case.execute.return_value = {"some": "data"}
        mock_repository.return_value = mock_use_case
        mock_get_weather_repository.return_value = mock_repository

        # Create a sample event
        event = {
            "resource": "/playlist",
            "other": "data"
        }

        # Call handler
        response = handler(event, None)
        expected_response = {
            'statusCode': 200,
            'body': '{"success": true, "message": "OK", "data": {"some": "data"}}'
        }
        self.assertEqual(response, expected_response)

    @patch('dependencies.get_weather_repository')
    def test_handler_not_implemented(self, mock_get_weather_repository):
        # Setup mock
        mock_repository = Mock()
        mock_use_case = Mock()
        mock_repository.return_value = mock_use_case
        mock_get_weather_repository.return_value = mock_repository

        # Create a sample event
        event = {
            "resource": "/nonexistent",
            "other": "data"
        }

        # Call handler
        response = handler(event, None)
        expected_response = {
            'statusCode': 404,
            'body': '{"success": false, "message": "Handler /nonexistent is not implemented", "data": {}}'
        }
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
