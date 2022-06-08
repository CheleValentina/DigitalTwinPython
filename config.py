class Settings:
    WEATHER_API_URL = (
        "http://api.weatherapi.com/v1/current.json?key=39180673f6ba415ea1395047220706&q={city}"
    )
    MODEL_FILENAME = "models/model.pickle"


settings = Settings()
