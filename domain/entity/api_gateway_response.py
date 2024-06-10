import json
from typing import Any, Dict
from domain.entity.api_gateway_response_body import ApiGatewayResponseBody


class ApiGatewayResponse:
    def __init__(self, status_code: int, body: ApiGatewayResponseBody):
        self.body = body
        self.status_code = status_code

    def generate_response(self) -> Dict[str, Any]:
        return {
            "statusCode": self.status_code,
            "headers": {"Access-Control-Allow-Methods": "GET"},
            "body": json.dumps(self.body.__dict__, indent=4)
        }
