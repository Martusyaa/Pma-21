from pyxtension.streams import stream

class Student:
    def __init__(self, name, surname, data_birthday, list_grade):
        self.name = name
        self.surname = surname
        self.data_birthday = data_birthday
        self.list_grade = list_grade

class Dekanat:
    def __init__(self):
        self.students = []

    def read_matrix_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    try:
                        parts = line.strip().split(':')
                        name_parts = parts[0].split()
                        first_name = name_parts[1]
                        last_name = name_parts[0]
                        birth_date, *grades = parts[1].split(', ')
                        list_grade = [int(i) for i in str.split(*grades)]
                        student = Student(first_name, last_name, birth_date, list_grade)
                        self.students.append(student)
                    except ValueError as e:
                        print(f"Неправильні дані: {e}")
                        continue
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка: {e}")

        if not self.students:
            print("Файл пустий.")

    def print_failed_students(self):
        results = stream(self.students).flatMap(lambda student: [(student, grade) for grade in student.list_grade if grade < 51])
        for result in results:
            student, grade = result
            print(f"{student.name} {student.surname} не склав сесію. Бал: {grade}")