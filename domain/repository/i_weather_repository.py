from abc import ABC, abstractmethod

from infra.model.weather.weather_model import WeatherModel

class IWeatherRepository(ABC):
    @abstractmethod
    def get_weather_termperature(self, city: str) -> WeatherModel:
        pass