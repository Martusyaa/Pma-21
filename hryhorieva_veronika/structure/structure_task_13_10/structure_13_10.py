class Student:
    name: str
    age: int
    surname: str
    date_birth: str
    marks: list
    students = []
    failed_students = []


    def read_from_file(self):
        with (open("input.txt") as file):
            lines = file.readlines()
            for i in lines:
                student = Student()
                line = i.split(",")
                obj_marks = [int(i) for i in line[-1].split(" ") if i.isdigit()]
                student.name = line[0]
                student.surname = line[1]
                try:
                    student.age = line[2]
                    assert int(student.age) > 0
                except AssertionError:
                    print(f'The age of the {student.surname} can not be negative')

                try:
                    student.date_birth = line[3]
                    date = student.date_birth.split(".")

                    assert len(date) == 3 and 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1 <= int(
                        date[2]) <= 2023
                except AssertionError as b:
                    print(f'The invalid date of birth of {student.surname}')

                student.marks = obj_marks
                self.students.append(student)


    def fail_exams(self):
        target = 51
        try:
            for i in self.students:
                assert sum(i.marks) <= 100
                if sum(i.marks) <= target:
                    print(f'{i.name, i.surname}, Average mark is: {round((sum(i.marks) / len(i.marks)), 2)}: failed!')
                    self.failed_students.append(i)
                else:
                    print(f'{i.name, i.surname}, Average mark is: {round((sum(i.marks) / len(i.marks)), 2)}: passed!')
        except AssertionError as b:
            print("One of the student has too high mark")

    def print_failed_students(self):
        print("\nList of students who failed:")
        for student in self.failed_students:
            print(
                f'{student.name}, {student.surname}, Average mark: {round((sum(student.marks) / len(student.marks)), 2)}')


students = Student()
students.read_from_file()
students.fail_exams()
students.print_failed_students()
