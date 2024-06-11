from services.requests.interface.i_requests import IRequests
import requests
from requests.models import Response


class Requests(IRequests):
    def get(self, url: str) -> Response:
        response = requests.get(url=url, headers={'User-Agent': 'Google Chrome'})
        return response