class InvalidHandlerException(Exception):
    """Raised when handler path doesnt exist"""

class MissingCityException(Exception):
    """Raised when city parameter is missing"""

class WeatherApiException(Exception):
    """Any problem that happens with weather api"""

class SpotifyApiException(Exception):
    """Any problem that happens with spotify api"""