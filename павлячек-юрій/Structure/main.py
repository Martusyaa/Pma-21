
import os
class Student:
    def __init__(self, first_name, last_name, date_of_birth, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.grades = grades


def read_students_from_file(file_path):
    students = []
    try:
        if os.path.getsize(file_path) == 0:
            print("File is empty:", file_path)
            return students

        with open(file_path) as file:
            for line in file:
                data = line.strip().split(',')
                first_name, last_name, date_of_birth, grade_str = data
                grades = [int(grade) for grade in grade_str.split()]
                student = Student(first_name, last_name, date_of_birth, grades)
                students.append(student)

        return students
    except FileNotFoundError:
        print("File is not found:", file_path)

def find_students_who_failed_session(students):
    failed_students = []

    for student in students:
        average_score = sum(student.grades) / len(student.grades)
        if average_score < 60:
            failed_students.append(student)

    return failed_students

FILE = 'students.txt'
students = read_students_from_file(FILE)
failed_students = find_students_who_failed_session(students)

if failed_students:
    print("Students who failed the session:")
    for student in failed_students:
        print(f"{student.first_name} {student.last_name}")

