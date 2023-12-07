from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
STUDENTS = {
    '1': {
        'name': 'Mark',
        'age': 23,
        'spec': 'math'
    },
    '2': {
        'name': 'Jane',
        'age': 20,
        'spec': 'biology'
    },
    '3': {
        'name': 'Peter',
        'age': 21,
        'spec': 'history'
    },
    '4': {
        'name': 'Kate',
        'age': 22,
        'spec': 'science'
    },
}

class StudentsList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        parser_copy = parser.copy()
        parser_copy.add_argument("name", required=True)
        parser_copy.add_argument("age", type=int, required=True)
        parser_copy.add_argument("spec", required=True)
        args = parser_copy.parse_args()

        student_id = str(int(max(STUDENTS.keys())) + 1)
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
        }
        return STUDENTS[student_id], 201

class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]

    def patch(self, student_id):
        parser_copy = parser.copy()
        parser_copy.add_argument("name")
        parser_copy.add_argument("age")
        parser_copy.add_argument("spec")
        args = parser_copy.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args["name"] is not None else student["name"]
            student["age"] = args["age"] if args["age"] is not None else student["age"]
            student["spec"] = args["spec"] if args["spec"] is not None else student["spec"]
            return student, 200

    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
            return '', 204

api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__ == "__main__":
    app.run(debug=True)

#?name=Mary&age=23&spec=programming
#?age=32

