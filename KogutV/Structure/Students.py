from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    first_name: str
    last_name: str
    date_of_birth: str
    grades: List[int]

def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            first_name = data[0]
            last_name = data[1]
            date_of_birth = data[2]
            grades = [int(grade) for grade in data[3:]] 
            student = Student(first_name, last_name, date_of_birth, grades)
            students.append(student)
    return students

