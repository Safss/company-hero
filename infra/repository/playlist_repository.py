from typing import Any, Dict
from domain.repository.i_playlist_repository import IPlayListRepository
from infra.datasource.i_external_playlist_datasource import IExternalPlayListDatasource


class PlayListRepository(IPlayListRepository):
    def __init__(self, datasource: IExternalPlayListDatasource):
        self.datasource = datasource

    def get_playlist(self, musical_genre: str) -> Dict[str, Any]:
        return self.datasource.get_playlist(musical_genre==musical_genre)