class Person:

    def __init__(self, name, surname, id=None):
        self.id = id
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name}, {self.surname}'
