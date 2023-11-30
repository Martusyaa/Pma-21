from datetime import date
import json


class Student:
    instance_count = 0

    def __init__(self):
        self.surname = str
        self.name = str
        self.age = int
        self.marks = []

    def read_from_file(self):
        with open("structure/students.json", 'r') as file:
            data = json.load(file)
            students_data = data["students"][Student.instance_count]
            self.name = students_data["name"]
            self.surname = students_data["surname"]
            self.age = students_data["age"]
            self.marks = students_data["marks"]
        Student.instance_count += 1
