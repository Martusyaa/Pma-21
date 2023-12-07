class Student:
    def __init__(self, name, surname, date_of_birth, grades):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.grades = grades


def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            name, surname, date_of_birth, grades_str = data[0], data[1], data[2], data[3:]
            grades = [int(grade) for grade in grades_str]


            if any(grade < 0 for grade in grades):
                raise ValueError("Оцінка не може бути від'ємною.")

            student = Student(name, surname, date_of_birth, grades)
            students.append(student)
    return students


def find_students_not_passed(students):
    failed_students = []
    for student in students:
        if any(grade < 60 for grade in student.grades):
            failed_students.append(student)
    return failed_students


def main():
    file_path = 'students.txt'
    try:
        students = read_students_from_file(file_path)
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    failed_students = find_students_not_passed(students)

    if len(failed_students) > 0:
        print("Студенти, які не склали сесію:")
        for student in failed_students:
            print(f"{student.name} {student.surname}")
    else:
        print("Усі студенти склали сесію.")


if name == "__main__":
    main()
