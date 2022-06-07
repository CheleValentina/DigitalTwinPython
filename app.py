from flask import Flask, jsonify
from flask_cors import CORS
from weather_api import get_data_for_city

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return "OK"


@app.route("/weather/<city>/", methods=["GET"])
def get_for_city(city):
    data = get_data_for_city(city)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
