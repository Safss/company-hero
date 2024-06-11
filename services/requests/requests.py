from typing import Any, Dict
from services.requests.interface.i_requests import IRequests
import requests
from requests.models import Response


class Requests(IRequests):
    def get(self, url: str, headers: Dict[str, Any] = {}) -> Response:
        response = requests.get(url=url, headers=headers)
        return response
    
    def post(self, url: str, header: str, payload: str):
        response = requests.post(url=url, headers=header, data=payload)
        return response