from abc import ABC, abstractmethod
from typing import Any, Dict

class IPlayListRepository(ABC):
    @abstractmethod
    def get_playlist(self, musical_genre: str) -> Dict[str, Any]:
        pass