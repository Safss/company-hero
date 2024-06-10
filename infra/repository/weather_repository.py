from domain.repository.i_weather_repository import IWeatherRepository
from infra.datasource.i_external_weather_datasource import IExternalWeatherDatasource


class WeatherRepository(IWeatherRepository):
    def __init__(self, datasource: IExternalWeatherDatasource):
        self.datasource = datasource

    def get_weather_termperature(self, city: str) -> int:
        return self.datasource.get_weather_termperature(city=city)