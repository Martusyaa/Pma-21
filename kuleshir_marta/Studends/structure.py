class Student:
    def __init__(self, stud_name, stud_surname, stud_birthdate, stud_grades):
        self.name = stud_name
        self.surname = stud_surname
        self.birthdate = stud_birthdate
        self.grades = stud_grades


students = []

try:
    with open('input.txt') as file:
        for line in file.readlines():
            data = line.strip().split(',')
            name, surname, birthdate, grades = data[0], data[1], data[2], list(map(int, data[3].split()))
            student = Student(name, surname, birthdate, grades)
            average_grade = sum(student.grades) / len(student.grades)
            if average_grade < 51:
                students.append(student)
    if not students:
        print("Усі студенти склали сесію!")
    else:
        print("Студенти, які не склали сесію:")
        for student in students:
            print(f"Ім'я: {student.name}, Прізвище: {student.surname}, Дата народження: {student.birthdate}, Оцінки: {student.grades}")
except FileNotFoundError:
    print("Файл не знайдено.")
