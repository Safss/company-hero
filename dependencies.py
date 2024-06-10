from external.weather_datasource import WeatherDatasource
from infra.repository.weather_repository import WeatherRepository

def get_weather_repository():
    datasource = WeatherDatasource()
    return WeatherRepository(datasource=datasource)