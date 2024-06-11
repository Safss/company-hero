from __future__ import annotations

import json
from typing import Any, Dict, Optional
from domain.entity.weather import Weather


class WeatherModel(Weather):
    @classmethod
    def from_dict(cls, weather_dict: Dict[str, Any]) -> Optional[WeatherModel]:
        if not weather_dict:
            return None
        return Weather(weather_dict)

    @classmethod
    def from_json(cls, weather_json: str) -> Optional[WeatherModel]:
        return cls.from_dict(json.loads(weather_json))