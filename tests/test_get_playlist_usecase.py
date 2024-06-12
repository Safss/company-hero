import unittest
from unittest.mock import MagicMock, patch
from application.get_playlist_usecase import GetPlaylistUseCase
from domain.errors.exceptions import MissingCityException

class TestGetPlaylistUseCase(unittest.TestCase):
    def setUp(self):
        self.weather_repository = MagicMock()
        self.playlist_repository = MagicMock()
        self.use_case = GetPlaylistUseCase(self.weather_repository, self.playlist_repository)

    def test_execute_with_missing_city(self):
        # Arrange
        event = {"queryStringParameters": {}}

        # Act & Assert
        with self.assertRaises(MissingCityException):
            self.use_case.execute(event)

    def test_execute_with_valid_city(self):
        # Arrange
        event = {"queryStringParameters": {"city": "New York"}}
        weather_data = {"main": {"temp": 20}}
        playlist_data = [{"name": "Song 1"}, {"name": "Song 2"}]

        self.weather_repository.get_weather_termperature.return_value = weather_data
        self.playlist_repository.get_playlist.return_value = playlist_data

        # Act
        result = self.use_case.execute(event)

        # Assert
        self.assertEqual(result["city"], "New York")
        self.assertEqual(result["temperature"], 20)
        self.assertEqual(result["playlist"], playlist_data)

    def test_get_city_temperature(self):
        # Arrange
        city = "New York"
        weather_data = {"main": {"temp": 20}}
        self.weather_repository.get_weather_termperature.return_value = weather_data

        # Act
        temperature = self.use_case.get_city_temperature(city)

        # Assert
        self.assertEqual(temperature, 20)

    def test_get_city_from_event(self):
        # Arrange
        event = {"queryStringParameters": {"city": "New York"}}

        # Act
        city = self.use_case.get_city_from_event(event)

        # Assert
        self.assertEqual(city, "New York")

if __name__ == '__main__':
    unittest.main()
