data_file="students.txt"
class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def read_students_from_file(data_file):
    students = []
    with open(data_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            first_name, last_name, birth_date = data[:3]
            grades = [int(grade) for grade in data[3:]]
            student = Student(first_name, last_name, birth_date, grades)
            students.append(student)
    return students

def find_students_not_passing(students):
    not_passing_students = []
    for student in students:
        average_grade = student.average_grade()
        if average_grade < 61:
            not_passing_students.append(student)
    return not_passing_students

students = read_students_from_file(data_file)
not_passing_students = find_students_not_passing(students)

if not_passing_students:
    for student in not_passing_students:
        print(f"{student.first_name} {student.last_name} не склав сесію. Середній бал: {student.average_grade()}")
else:
    print("Усі студенти склали сесію!")

