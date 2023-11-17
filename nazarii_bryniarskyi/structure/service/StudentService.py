from nazarii_bryniarskyi.structure.model.Student import Student
import re

class StudentService:

    def __init__(self):
        self.list_of_students = []
        self.SEMICOLON = ';'
        self.COMA = ','
        self.STUDENTS_INFO = "/Users/nazariybrynyarsky/Desktop/Python/Pma-21eewewweewewwewe/nazarii_bryniarskyi/structure/data/students-info.txt"
        self.read_students()


    def read_students(self) -> None:
        try:
            with open(self.STUDENTS_INFO) as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(self.SEMICOLON)
                    if len(parts) == 4:
                        name, surname, date_of_birth, grades_array = parts
                        grades = [int(grade) for grade in re.findall(r'\d+', grades_array)]
                        self.list_of_students.append(Student(name, surname, date_of_birth, grades))
                    else:
                        print(f"Invalid data in line: {line}")
        except FileNotFoundError:
            print(f"File '{self.STUDENTS_INFO}' was not found.")


    def print_all_students(self) -> None:
        print("All students:")
        for i in range(len(self.list_of_students)):
            print(f"{i+1}. {self.list_of_students[i]}")


    def find_losers(self):
        losers = []
        for student in self.list_of_students:
            grades = student.list_of_grades
            if any(grade < 51 for grade in grades):
                losers.append(student)
                continue
        return losers
