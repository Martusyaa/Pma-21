

from flask import Flask, jsonify, request
import json
import uuid


app = Flask(__name__)

class Message:
    def __init__(self, message_id, text):
        self.message_id = message_id
        self.text = text

def load_initial_data():
    try:
        with open('data_base.json', 'r') as file:
            data = json.load(file)
            return [Message(obj['message_id'], obj['text']) for obj in data]
    except FileNotFoundError:
        return []

def save_data_to_json():
    data_to_save = [{"message_id": message.message_id, "text": message.text} for message in messages]
    with open('data_base.json', 'w') as file:
        json.dump(data_to_save, file)

messages = load_initial_data()


@app.route('/messages', methods=['POST'])
def create_message():
    new_message_data = request.json
    message_id = str(uuid.uuid4())
    new_message = Message(message_id, new_message_data['text'])
    messages.append(new_message)
    save_data_to_json()
    return jsonify({"message": "Повідомлення створено успішно"}), 201

@app.route('/messages/<message_id>', methods=['PATCH'])
def update_message(message_id):
    updated_message_data = request.json
    for message in messages:
        if message.message_id == message_id:
            message.text = updated_message_data['text']
            save_data_to_json()
            return jsonify({"message": "Повідомлення оновлено успішно"})
    return jsonify({"error": "Повідомлення не знайдено"}), 404

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify([{"message_id": message.message_id, "text": message.text} for message in messages])

@app.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    for message in messages:
        if message.message_id == message_id:
            messages.remove(message)
            save_data_to_json()
            return jsonify({"message": f"Повідомлення з ID {message_id} видалено успішно"})
    return jsonify({"error": "Повідомлення не знайдено"}), 404

if __name__ == '__main__':
      app.run(debug=True)


