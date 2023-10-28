class Library:
    def __init__(self, name, author, number_pages):
        self.name = name
        self.author = author
        self.number_pages = number_pages

    def __str__(self):
        return f"Ім'я: {self.name}, Автор: {self.author}, Кількість сторінок: {self.number_pages}"