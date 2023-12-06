class User:

    def __init__(self, username, name, surname, age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"({self.username}, {self.name}, {self.surname}, {self.age})"
