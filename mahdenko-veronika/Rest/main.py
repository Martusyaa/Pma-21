import sys

from flask import Flask, request, jsonify
import json
import random


app = Flask(__name__)

class Car:
    def __init__(self, car_id, name, year):
        self.car_id = car_id
        self.name = name
        self.year = year

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "name": self.name,
            "year": self.year
        }

class CarAPI:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open("cars.json", "r") as file:
                data = json.load(file)
                self.cars = [Car(car["car_id"], car["name"], car["year"]) for car in data]
        except FileNotFoundError:
            print("File not found")
            self.cars = []

    def save_data(self):
        data_to_save = [car.to_dict() for car in self.cars]
        with open("cars.json", "w") as file:
            json.dump(data_to_save, file)

    def get_cars(self):
        return [car.to_dict() for car in self.cars]

    def create_car(self, data):
        car_id = random.randint(1, 10000)
        car = Car(car_id, data["name"], data["year"])
        self.cars.append(car)
        self.save_data()
        return car.to_dict()

    def update_car(self, car_id, data):
        car = self.find_car_by_id(car_id)
        if car is not None:
            if "name" in data:
                car.name = data["name"]
            if "year" in data:
                car.year = data["year"]
            self.save_data()
            return car.to_dict()
        return None

    def delete_car(self, car_id):
        car = self.find_car_by_id(car_id)
        if car is not None:
            self.cars = [c for c in self.cars if c.car_id != car_id]
            self.save_data()
            return car.to_dict()
        return None

    def find_car_by_id(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
        return None

car_api = CarAPI()

@app.route('/cars', methods=['GET'])
def get_car():
    car_id = None
    print(request.headers, file=sys.stderr)
    print(request.headers.get('id'),file=sys.stderr)
    if 'car_id' in request.args:
        car_id = request.args.get('car_id')
    elif 'id' in request.headers:
        car_id = request.headers.get('id')

    if car_id is None:
        return jsonify({"message": "Car ID not found in request"}), 400

    car = car_api.find_car_by_id(int(car_id))
    if car is not None:
        return jsonify(car.to_dict())
    return jsonify({"message": "Car not found"}), 404

@app.route('/cars', methods=['POST'])
def create_car():
    try:
        data = request.get_json()
        if "name" not in data or "year" not in data:
            raise KeyError("Name and year are required fields")
        car = car_api.create_car(data)
        return jsonify(car)
    except (KeyError) as e:
        return jsonify({"message": str(e)}), 400

@app.route('/cars/<int:car_id>', methods=['PATCH'])
def update_car(car_id):
    data = request.get_json()
    updated_car = car_api.update_car(car_id, data)
    if updated_car is not None:
        return jsonify(updated_car)
    return jsonify({"message": "Car not found"}), 404

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    deleted_car = car_api.delete_car(car_id)
    if deleted_car is not None:
        return jsonify(deleted_car), 200
    return jsonify({"message": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)