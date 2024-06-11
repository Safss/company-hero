from abc import ABC, abstractmethod


class IRequests(ABC):
    @abstractmethod
    def get(self, url: str):
        pass