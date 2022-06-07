import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS

from ai_model import load_model
from predictions import get_prediction
from weather_api import get_data_for_city

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return "OK"


@app.route("/weather/<city>/", methods=["GET"])
def get_for_city(city):
    data = get_data_for_city(city)

    # TODO replace theoretical power
    t_p = 1500

    prediction = get_prediction(data["wind_mps"], data["wind_degree"], t_p)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run()
