import os


URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
API_KEY_WEATHER = str(os.getenv("weatherApikey", ""))
SPOTIFY_URL_AUTH = "https://accounts.spotify.com/api/token"
SPOTIFY_URL_SEARCH = "https://api.spotify.com/v1/search"
SPOTIFY_CLIENT_ID = str(os.getenv("spotifyClientId", ""))
SPOTIFY_CLIENT_SECRET = str(os.getenv("spotifyClientSecret", ""))