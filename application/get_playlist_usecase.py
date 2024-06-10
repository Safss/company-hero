from typing import Any, Dict

from domain.repository.i_weather_repository import IWeatherRepository

class GetPlaylistUseCase:
    def __init__(self, weather_repository: IWeatherRepository):
        self.weather_repository = weather_repository

    def execute(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return {"temperatura": self.weather_repository.get_weather_termperature(city='SP')}