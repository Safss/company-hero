from typing import Any, Dict, List, Optional
from domain.entity.playlist import PlayList
from domain.errors.exceptions import MissingCityException
from domain.repository.i_playlist_repository import IPlayListRepository

from domain.repository.i_weather_repository import IWeatherRepository

class GetPlaylistUseCase:
    def __init__(self, weather_repository: IWeatherRepository, playlist_repository: IPlayListRepository):
        self.weather_repository = weather_repository
        self.playlist_repository = playlist_repository

    def execute(self, event: Dict[str, Any]) -> Dict[str, Any]:
        city = self.get_city_from_event(event)
        if not city:
            raise MissingCityException("Parameter city is missing")
        
        playlist = PlayList(city=city)
        playlist.temperature = self.get_city_temperature(city=city)
        playlist.playlist = self.get_playlist(playlist.musical_genre)

        return playlist.generate_playlist_response()
    
    def get_city_temperature(self, city: str) -> int:
        weather = self.weather_repository.get_weather_termperature(city)
        return weather.main.get('temp', None)
    
    def get_playlist(self, musical_genre: str) -> List[Dict[str, Any]]:
        return self.playlist_repository.get_playlist(musical_genre)
    
    def get_city_from_event(self, event: Dict[str, Any]) -> Optional[str]:
        queryString = event.get("queryStringParameters", {})
        if queryString:
            return queryString.get("city", None)