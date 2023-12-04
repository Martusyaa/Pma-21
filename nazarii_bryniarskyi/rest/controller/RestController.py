from flask import Flask, request
from nazarii_bryniarskyi.rest.service.PersonService import PersonService


class RestController:

    app = Flask(__name__)

    @staticmethod
    @app.route('/api/persons', methods=['GET'])
    def findAll():
        return PersonService.findAll()


    @staticmethod
    @app.route('/api/persons/<int:id>', methods=['GET'])
    def findById(id):
        return PersonService.findById(id)


    @staticmethod
    @app.route('/api/persons/save', methods=['POST'])
    def save():
        data = request.get_json()
        return PersonService.save(data['name'], data['surname'])


    @staticmethod
    @app.route('/api/persons/update', methods=['PATCH'])
    def update():
        data = request.get_json()
        return PersonService.update(data['id'], data['name'], data['surname'])


    @staticmethod
    @app.route('/api/persons/delete', methods=['DELETE'])
    def delete():
        data = request.get_json()
        return PersonService.delete(data['id'])


if __name__ == '__main__':
    RestController().app.run(port=8888)
