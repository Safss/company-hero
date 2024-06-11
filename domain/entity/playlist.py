from typing import Any, Dict


class PlayList:
    def __init__(self, city: str):
        self.city = city
        self._temperature = 0
        self._musical_genre = ""
        self._playlist = []

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int):
        self._temperature = temperature
        self.define_musical_genre(temperature)

    @property
    def playlist(self) -> Dict[str, Any]:
        return self._playlist
    
    @playlist.setter
    def playlist(self, playlist: Dict[str, Any]):
        self._playlist = playlist

    @property
    def musical_genre(self) -> str:
        return self._musical_genre
    
    @musical_genre.setter
    def musical_genre(self, musical_genre: str):
        self._musical_genre = musical_genre


    def define_musical_genre(self, temperature: int):
        if(temperature < 10):
            self._musical_genre = "CLASSIC"
        elif(temperature >= 10 and temperature <= 25):
            self._musical_genre = "ROCK"
        else:
            self._musical_genre = "POP"

    def generate_playlist_response(self):
        return {
            "city": self.city,
            "temperature": self._temperature,
            "musical_genre": self._musical_genre,
            "playlist": self._playlist
        }
        

