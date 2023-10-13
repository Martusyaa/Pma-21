class Student:
    def __init__(self, name, surname, data_birthday, list_grade):
        self.name = name
        self.surname = surname
        self.data_birthday = data_birthday
        self.list_grade = list_grade

    @staticmethod
    def read_matrix_from_file(filename):
        students = []
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
                        students.append(student)
                    except ValueError as e:
                        print(f"Неправильні дані: {e}")
                        continue
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка: {e}")

        if not students:
            print("Файл пустий.")

        return students
    # @staticmethod
    # def print_failed_students(students):
    #     for i in students.list_grade:
    #         if i < 51:
    #             print(f"{students.first_name} {students.last_name} не склав сесію")

    @staticmethod
    def print_failed_students(students):
        for student in students:
            for grade in student.list_grade:
                failed = grade < 51
                if failed:
                    print(f"{student.name} {student.surname} не склав сесію")