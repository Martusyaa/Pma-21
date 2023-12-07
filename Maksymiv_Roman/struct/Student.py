class Student:


    def __init__(self, name="Не вказано", surname="Не вказано", date_of_birth="Не вказано", marks="Не вказано"):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.marks = marks
        self.has_passed = self.exam_validation()


    def exam_validation(self):
        if min(self.marks) >= 51:
            return 1
        else:
            return 0


    def __str__(self):
        return f'{self.name} {self.surname}, {self.date_of_birth}, {"Passed" if self.has_passed else "Failed"}'