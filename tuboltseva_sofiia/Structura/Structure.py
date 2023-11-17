class Student:
    def __init__(self, name, surname, date, rating):
        self.name = name
        self.surname = surname
        self.date = date
        self.rating = rating
def rid_student(file):
    students = []
    try:
        with open(file, 'r') as file_student:
            for row in file_student:
                try:
                    parts = row.strip().split(',')
                    if len(parts) < 8:
                        print("дані не коректні")
                        continue
                    name, surname, date = parts[0], parts[1], parts[2]
                    rating = [int(i) for i in parts[3:]]
                    new_student = Student(name, surname, date, rating)
                    students.append(new_student)
                except ValueError as e:
                  print(f"Неправильні дані: {e}")
                  continue

    except FileNotFoundError:
       print(f"Файл {file} не знайдено.")
    except Exception as e:
       print(f"Виникла помилка: {e}")

    return students
def talon(students):
    for student in students:
        for a_rating in student.rating:
        #ser_rating = sum(map(int, student.rating))/ len(student.rating)
            if a_rating < 51:
               print(f'{student.name} {student.surname}: бал {a_rating}, не склав іспит')

try:
    file_students = 'students.txt'
    students = rid_student(file_students)
    talon(students)
except FileNotFoundError:
    print(f"Файл '{file_students}' не знайдено.")