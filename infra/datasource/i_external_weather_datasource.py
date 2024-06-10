from abc import ABC, abstractmethod

class IExternalWeatherDatasource(ABC):
    @abstractmethod
    def get_weather_termperature(self, city: str) -> int:
        pass