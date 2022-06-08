from flask import Flask, jsonify
from flask_cors import CORS
from predictions import get_prediction
from weather_api import get_data_for_city

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return "OK"


@app.route("/weather/<city>/<theoretical_power>/", methods=["GET"])
def get_for_city(city: str, theoretical_power: int):
    data = get_data_for_city(city)

    prediction = get_prediction(data["wind_mps"], data["wind_degree"], theoretical_power)
    return jsonify([prediction, round(data["wind_mps"], 2), round(data["wind_degree"], 2)])


if __name__ == "__main__":
    app.run()
