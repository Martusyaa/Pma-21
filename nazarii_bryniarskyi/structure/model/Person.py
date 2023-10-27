class Person:

    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth


    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Date of birth: {self.date_of_birth}"
