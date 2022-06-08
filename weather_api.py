import json
from pprint import pprint

import requests

from config import settings


def get_data_for_city(city: str):
    response = requests.get(settings.WEATHER_API_URL.format(city=city))
    data = json.loads(response.text)["current"]

    return {"wind_mps": data["wind_kph"] * 5 / 18, "wind_degree": data["wind_degree"]}
