INPUT_FILE_NAME = "students.txt"
FILE_NOT_FOUND = "File not found"
ERROR = "File is empty"
ERROR2 = "Invalid data format in line"
from pyxtension.streams import stream

class Student:
    def __init__(self, first_name, last_name, birthday, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.marks = marks
    def display(self):
        for mark in self.marks:
            if mark < 3:
                return False
            else:
                return True

class Decanat:
    def check(self, student):
        if student.display():
            return f"Student {student.first_name.upper()} {student.last_name.upper()} pass the session."
        else:
            return f"Student {student.first_name.upper()} {student.last_name.upper()} failed the session."
    def print_results(self, students):
        results = stream(students).map(self.check)
        for result in results:
            print(result)

students = []
try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise FileNotFoundError(ERROR)
        for line in lines:
            data = line.strip().split(' ')
            if len(data) < 4:
                print('Error:', ValueError(ERROR2))
            else:
                first_name = data[0]
                last_name = data[1]
                birth_date = data[2]
                marks = [int(mark) for mark in data[3].split(',')]
                student = Student(first_name, last_name, birth_date, marks)
                students.append(student)

except FileNotFoundError:
    print('Error:', FILE_NOT_FOUND)
except ValueError as e:
    print('Error:', e)
except Exception as e:
    print('Error:', e)

dean_office_instance = Decanat()
dean_office_instance.print_results(students)