from external.playlist_datasource import PlayListDatasource
from external.weather_datasource import WeatherDatasource
from infra.repository.playlist_repository import PlayListRepository
from infra.repository.weather_repository import WeatherRepository
from services.requests.requests import Requests

def get_weather_repository():
    requests = Requests()
    datasource = WeatherDatasource(request_service=requests)
    return WeatherRepository(datasource=datasource)

def get_playlist_repository():
    requests = Requests()
    datasource = PlayListDatasource(request_service=requests)
    return PlayListRepository(datasource=datasource)