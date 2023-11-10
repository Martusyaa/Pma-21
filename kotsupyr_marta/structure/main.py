from pyxtension.streams import stream
data_file = "students.txt"
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
class Dekanat:
    def check_session_result(self, student):
        average_grade = student.average_grade()
        if average_grade >= 61:
            return f"{student.first_name} {student.last_name} склав сесію. Середній бал: {average_grade}"
        else:
            return f"{student.first_name} {student.last_name} не склав сесію. Середній бал: {average_grade}"

    def print_session_results(self, students):
        results = stream(students).map(self.check_session_result)
        for result in results:
            print(result)

def read_students_from_file(data_file):
    students = []
    with open(data_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            first_name, last_name, birth_date = data[:3]
            grades = [int(grade) for grade in data[3:]]
            student = Student(first_name, last_name, birth_date, grades)
            students.append(student)
    return students

def find_students_not_passing(students):
    return stream(students).filter(lambda student: student.average_grade() <= 61)

students = read_students_from_file(data_file)
dean_office_instance = Dekanat()
not_passing_students = find_students_not_passing(students)

if not_passing_students:
    dean_office_instance.print_session_results(not_passing_students)
else:
    print("Усі студенти склали сесію!")
