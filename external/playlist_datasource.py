from typing import Any, Dict
from infra.datasource.i_external_playlist_datasource import IExternalPlayListDatasource


class PlayListDatasource(IExternalPlayListDatasource):
    def __init__(self) -> None:
        super().__init__()

    def get_playlist(self, musical_genre: str) -> Dict[str, Any]:
        return [
            {"musica": "oyeah"},
            {"musica": "HEHEHE"}
        ]