from typing import Any, Dict, Optional
from domain.entity.playlist import PlayList
from domain.errors.exceptions import MissingCityException

from domain.repository.i_weather_repository import IWeatherRepository

class GetPlaylistUseCase:
    def __init__(self, weather_repository: IWeatherRepository):
        self.weather_repository = weather_repository

    def execute(self, event: Dict[str, Any]) -> Dict[str, Any]:
        city = self.get_city_from_event(event)
        if not city:
            raise MissingCityException("Parameter city is missing")
        
        playlist = PlayList(city=city)
        playlist.temperature = self.get_city_temperature(city=city)

        return playlist.generate_playlist_response()
    
    def get_city_temperature(self, city: str) -> int:
        return self.weather_repository.get_weather_termperature(city=city)
    
    def get_city_from_event(self, event: Dict[str, Any]) -> Optional[str]:
        queryString = event.get("queryStringParameters", {})
        if queryString:
            return queryString.get("city", None)