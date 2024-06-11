import os


URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
API_KEY_WEATHER = str(os.getenv("weatherApikey", ""))