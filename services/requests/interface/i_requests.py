from abc import ABC, abstractmethod
from typing import Any, Dict


class IRequests(ABC):
    @abstractmethod
    def get(self, url: str, headers: Dict[str, Any]):
        pass

    @abstractmethod
    def post(self, url: str, header: str, payload: str):
        pass