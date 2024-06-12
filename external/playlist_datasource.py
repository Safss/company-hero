import json
import logging
from typing import Any, Dict, List
from config.globals import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_URL_AUTH, SPOTIFY_URL_SEARCH
from domain.errors.exceptions import SpotifyApiException
from infra.datasource.i_external_playlist_datasource import IExternalPlayListDatasource
from services.requests.interface.i_requests import IRequests


class PlayListDatasource(IExternalPlayListDatasource):
    def __init__(self, request_service: IRequests) -> None:
        self.request_service = request_service
        super().__init__()

    def get_playlist(self, musical_genre: str) -> List[Dict[str, Any]]:
        try:
            token = self.get_token_request()
            url = f'{SPOTIFY_URL_SEARCH}?q=genre:{musical_genre}&type=playlist'
            spotify_response = self.request_service.get(url=url, headers={'Authorization': f'Bearer {token}'})
            if spotify_response.status_code != 200:
                logging.warning(f"[PlayListDatasource][get_playlist]: not found playlist {musical_genre}")
                raise SpotifyApiException("not possible to access spotify API")
            return json.loads(spotify_response.text).get("playlists", {}).get("items", [])
        except Exception as error:
            logging.error(f"[PlayListDatasource][get_playlist][ERROR]: {str(error)}")
            raise SpotifyApiException(str(error))
    
    def get_token_request(self) -> str:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = f'grant_type=client_credentials&client_id={SPOTIFY_CLIENT_ID}&client_secret={SPOTIFY_CLIENT_SECRET}'
        response = self.request_service.post(url=SPOTIFY_URL_AUTH, header=headers, payload=payload)
        return json.loads(response.text).get("access_token", None)