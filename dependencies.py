from external.playlist_datasource import PlayListDatasource
from external.weather_datasource import WeatherDatasource
from infra.repository.playlist_repository import PlayListRepository
from infra.repository.weather_repository import WeatherRepository

def get_weather_repository():
    datasource = WeatherDatasource()
    return WeatherRepository(datasource=datasource)

def get_playlist_repository():
    datasource = PlayListDatasource()
    return PlayListRepository(datasource=datasource)