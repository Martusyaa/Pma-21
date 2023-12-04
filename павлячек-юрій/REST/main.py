from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

cars = []


def load_data():
    try:
        with open("cars.json", "r") as file:
            cars.extend(json.load(file))
    except FileNotFoundError:
        print("File not found")


def save_data():
    with open("cars.json", "w") as file:
        json.dump(cars, file)


def find_car_by_name(car_name):
    return next((car for car in cars if car["name"] == car_name), None)


@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)


@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    if not all(key in data for key in ("name", "model", "year")):
        return jsonify({"message": "Name, model, and year are required fields"}), 400

    car = {"name": data["name"], "model": data["model"], "year": data["year"]}
    cars.append(car)
    save_data()

    return jsonify(car)


@app.route('/cars/<string:car_name>', methods=['PATCH'])
def update_car(car_name):
    data = request.get_json()
    car = find_car_by_name(car_name)

    if car:
        car.update({key: data.get(key, car[key]) for key in ("model", "year")})
        save_data()
        return jsonify(car)

    return jsonify({"message": "Car not found"}), 404


@app.route('/cars/<string:car_name>', methods=['DELETE'])
def delete_car(car_name):
    car = find_car_by_name(car_name)

    if car:
        cars.remove(car)
        save_data()
        return jsonify(car), 200

    return jsonify({"message": "Car not found"}), 404


if __name__ == '__main__':
    load_data()
    app.run(debug=True)
