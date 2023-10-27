from nazarii_bryniarskyi.structure.model.Person import Person

class Student(Person):

    def __init__(self, name, surname, date_of_birth, list_of_grades):
        super().__init__(name, surname, date_of_birth)
        self.list_of_grades = list_of_grades


    def __str__(self):
        return super().__str__() + f", List of grades: {self.list_of_grades}"
