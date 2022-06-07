from pprint import pprint

from config import settings
import requests
import json


def get_data_for_city(city: str):
    response = requests.get(settings.WEATHER_API_URL.format(city=city))
    data = json.loads(response.text)["current"]

    pprint(data)
    return {"wind_mps": data["wind_kph"] * 5 / 18, "wind_degree": data["wind_degree"]}
