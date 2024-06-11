from typing import Any, Dict, List


class Weather():
    def __init__(self, dicionario):
        self.coord: Dict[str, Any] = dicionario.get("coord")
        self.weather: List[Dict[str, Any]] = dicionario.get("weather")
        self.base: str = dicionario.get("base")
        self.main: Dict[str, Any] = dicionario.get("main")
        self.visibility: int = dicionario.get("visibility")
        self.wind: Dict[str, Any] = dicionario.get("wind")
        self.clouds: Dict[str, Any] = dicionario.get("clouds")
        self.dt: int = dicionario.get("dt")
        self.sys: Dict[str, Any] = dicionario.get("sys")
        self.timezone: int = dicionario.get("timezone")
        self.id: int = dicionario.get("id")
        self.name: str = dicionario.get("name")
        self.cod: int = dicionario.get("cod")