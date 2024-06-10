from abc import ABC, abstractmethod

class IWeatherRepository(ABC):
    @abstractmethod
    def get_weather_termperature(self, city: str) -> int:
        pass