from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IPlayListRepository(ABC):
    @abstractmethod
    def get_playlist(self, musical_genre: str) -> List[Dict[str, Any]]:
        pass