class Student:
    def __init__(self, data):
        self.first_name, self.last_name, self.birth_date, grades_str = data
        self.grades = [int(grade.strip()) for grade in grades_str.split()]


    def has_passed_session(self):
        return all(grade >= 51 for grade in self.grades)

def find_students_who_failed_session(file_name):
    failed_students = []

    try:
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) != 4:
                    print("Invalid data format in the file.")
                    continue
                student = Student(data)

                if not student.has_passed_session():
                    failed_students.append(student)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

    if failed_students:
        print("Students who failed the session:")
        for student in failed_students:
            print(f"Name: {student.first_name}\nLast Name: {student.last_name}\nBirth date: {student.birth_date}")
    else:
        print("No students failed the session.")
find_students_who_failed_session('students.txt')


