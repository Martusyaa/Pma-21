from flask import Flask, request, jsonify
import json

app = Flask(__name__)
data_file = "data.json"
keys_file = "keys.json"

class DataStorage:
    def __init__(self):
        self.data = {}

    def get_data(self):
        return self.data

    def update_data(self, new_data):
        self.data.update(new_data)

    def save_data(self, filename):
        try:
            with open(filename, "w") as file:
                json.dump(self.data, file)
        except Exception as e:
            raise Exception(f"Error saving data to file: {str(e)}")

    def delete_data(self, filename):
        try:
            if self.data:
                self.data = {}
                self.save_data(filename)
        except Exception as e:
            raise Exception(f"Error deleting data: {str(e)}")

    def read_keys_data(self, filename):
        try:
            with open(filename, "r") as file:
                keys_data = json.load(file)
                return keys_data
        except Exception as e:
            raise Exception(f"Error reading keys data from file: {str(e)}")

data_storage = DataStorage()

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        return jsonify(data_storage.get_data())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def save_data():
    try:
        request_data = request.get_json()
        data_storage.update_data(request_data)
        data_storage.save_data(data_file)
        return jsonify({"message": "Data saved successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['PATCH'])
def update_data():
    try:
        request_data = request.get_json()
        data_storage.update_data(request_data)
        data_storage.save_data(data_file)
        return jsonify({"message": "Data updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['DELETE'])
def delete_data():
    try:
        data_storage.delete_data(data_file)
        return jsonify({"message": "Data deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/keys', methods=['GET'])
def get_keys_data():
    try:
        keys_data = data_storage.read_keys_data(keys_file)
        return jsonify(keys_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
#postman