import logging
from typing import Any, Dict, Optional
from application.get_playlist_usecase import get_playlist_usecase
from domain.entity.api_gateway_response import ApiGatewayResponse
from domain.entity.api_gateway_response_body import ApiGatewayResponseBody

from domain.errors.exceptions import InvalidHandlerException

api_handlers = {
    "/playlist": get_playlist_usecase
}

def not_implemented(event: Dict[str, Any]):
    event_path = event.get("resource")
    raise InvalidHandlerException(f"Handler {event_path} is not implemented")

def main(event, context) -> Optional[Dict[str, Any]]:
    event_path = event.get("resource")
    event_handler = api_handlers.get(event_path, not_implemented)
    return event_handler(event)


def handler(event, context) -> Dict[str, Any]:
    try:
        response = main(event, context)
        print(response)
        return ApiGatewayResponse(
            status_code = 200,
            body=ApiGatewayResponseBody(success=True, message="OK", data=response)
        ).generate_response()
    
    except Exception as error:
        logging.exception(f"[api][handler][error]: {error}")
        return ApiGatewayResponse(
            status_code = 404,
            body=ApiGatewayResponseBody(success=False, message=str(error), data={})
        ).generate_response()
