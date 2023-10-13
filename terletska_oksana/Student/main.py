class Student:
    def __init__(self, name, surname, date_of_birthday, grades_list):
        self.name = name
        self.surname = surname
        self.date_of_birthday = date_of_birthday
        self.grades_list = grades_list

    def notPassSession(self):
        for grade in self.grades_list:
            if grade < 51:
                return True
        return False


def readStudentsFromFile(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                name = data[0]
                surname = data[1]
                date_of_birthday = data[2]
                grades_list = [int(mark) for mark in data[3:]]
                student = Student(name, surname, date_of_birthday, grades_list)
                students.append(student)
        return students
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def printStudents(students):
    for student in students:
        if student.notPassSession():
            print(f'Студент {student.name} {student.surname} не склав сесію.')

students = readStudentsFromFile('students.txt')
printStudents(students)