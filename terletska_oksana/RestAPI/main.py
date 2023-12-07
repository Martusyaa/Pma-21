from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

PLANTS = {
    '1': {'name': 'snowdrop ', 'height': 10, 'color': 'white'},
    '2': {'name': 'acacia', 'height': 3000, 'color': 'white'},
    '3': {'name': 'peony', 'height': 100, 'color': 'red'},
    '4': {'name': 'cornflower', 'height': 100, 'color': 'blue'},
}

parser = reqparse.RequestParser()


class PlantsList(Resource):
    def get(self):
        return PLANTS

    def post(self):
        if PLANTS == None:
            return "List plants is none.", 404
        parser.add_argument("name")
        parser.add_argument("height")
        parser.add_argument("color")
        args = parser.parse_args()
        plant_id = str(int(max(PLANTS.keys())) + 1)
        # plant_id = '%i' % plant_id
        PLANTS[plant_id] = {
            "name": args["name"],
            "height": args["height"],
            "color": args["color"],
        }
        return PLANTS[plant_id], 201


class Plant(Resource):
    def get(self, plant_id):
        if plant_id not in PLANTS:
            return 'Not found', 404
        else:
            return PLANTS[plant_id]

    def patch(self, plant_id):
        parser.add_argument("name")
        parser.add_argument("height")
        parser.add_argument("color")
        args = parser.parse_args()
        if plant_id not in PLANTS:
            return 'Record not found',404
        else:
            plant = PLANTS[plant_id]
            plant["name"] = args["name"] if args["name"] is not None else plant["name"]
            plant["height"] = args["height"] if args["height"] is not None else plant["height"]
            plant["color"] = args["color"] if args["color"] is not None else plant["color"]
            return plant, 200

    def delete(self, plant_id):
        if plant_id not in PLANTS:
            return "Not found", 404
        else:
            del PLANTS[plant_id]
            return '', 204


api.add_resource(PlantsList, '/plants/')
api.add_resource(Plant, '/plants/<plant_id>')

if __name__ == "__main__":
    app.run(debug=True)
