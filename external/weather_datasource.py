from infra.datasource.i_external_weather_datasource import IExternalWeatherDatasource


class WeatherDatasource(IExternalWeatherDatasource):
    def __init__(self) -> None:
        super().__init__()

    def get_weather_termperature(self, city: str) -> int:
        return 25