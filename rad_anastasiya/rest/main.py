from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pymongo
from bson import json_util

app = Flask(__name__)
api = Api(app)

DB_URL = "mongodb://localhost:27017/"
parser = reqparse.RequestParser()
parser.add_argument("password")
parser.add_argument('name')
parser.add_argument('surname')

user = pymongo.MongoUser(DB_URL)
db = user["usersdb"]
collection = db["users"]

class userList(Resource):
    def get(self):
        users = list(collection.find({}, {'_id': 0}))
        return users

    def post(self):
        password = request.json.get('password')
        name = request.json.get('name')
        surname = request.json.get('surname')

        if name is None or surname is None or id is None:
            return {'message': 'Missing data. Both name and surname and password are required.'}, 400

        user = {'password': password,'name': name, 'surname': surname}
        collection.insert_one(user)
        return {'message': "user added."}, 201

class user(Resource):
    def get(self, password):
        user = collection.find_one({"password": password}, {'_id': 0})
        if user:
            return json_util.dumps(user)
        return {'message': 'user not found'}, 404

    def patch(self, password):
        user = collection.find_one({"password": password})
        if user:
            update_data = request.json
            collection.update_one({"password": password}, {"$set": update_data})
            return {"message": "user updated."}
        return {'message': 'user not found'}, 404

    def delete(self, password):
        user = collection.find_one({"password": password})
        if user:
            collection.delete_one({"password": password})
            return {'message': 'user deleted'}
        return {'message': 'user not found'}, 404

api.add_resource(userList, '/users')
api.add_resource(user, '/users/<int:password>')

if __name__ == "__main__":
    app.run(debug=True)