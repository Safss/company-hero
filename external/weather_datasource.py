from config.globals import API_KEY_WEATHER, URL_WEATHER
from domain.errors.exceptions import WeatherApiException
from infra.datasource.i_external_weather_datasource import IExternalWeatherDatasource
from infra.model.weather.weather_model import WeatherModel
from services.requests.interface.i_requests import IRequests

class WeatherDatasource(IExternalWeatherDatasource):
    def __init__(self, request_service: IRequests) -> None:
        self.request_service = request_service
        super().__init__()

    def get_weather_termperature(self, city: str) -> WeatherModel:
        url = f"{URL_WEATHER}?q={city}&appid={API_KEY_WEATHER}&units=metric"
        try:
            response = self.request_service.get(url)
            if response.status_code != 200:
                raise WeatherApiException("not possible to access weather API")
            return WeatherModel.from_json(response.text)
        except Exception as error:
            raise WeatherApiException(str(error))