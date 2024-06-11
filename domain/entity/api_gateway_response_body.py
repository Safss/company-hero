from typing import Dict, Any, Optional


class ApiGatewayResponseBody():
    def __init__(self, success: bool, message: str, data: Optional[Dict[str, Any]]):
        self.success = success
        self.message = message
        self.data = data