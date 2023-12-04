class Library:
    def __init__(self):
        self.books = {}

    def display_books(self):
        print("Бібліотека:")
        for book_id, book_info in self.books.items():
            self.print_book_info(book_id, book_info)

    def print_book_info(self, book_id, book_info):
        print(f"Книга {book_id}:")
        print(f"  Назва: {book_info['назва']}")
        print(f"  Автор: {book_info['автор']}")
        print(f"  Рік: {book_info['рік']}")
        print(f"  Жанр: {book_info['жанр']}")
        print()

    def add_book(self, book_id, title, author, year, genre):
        self.books[book_id] = {"назва": title, "автор": author, "рік": year, "жанр": genre}
        print(f"Книга {book_id} додана до бібліотеки.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Книга {book_id} видалена з бібліотеки.")
        else:
            print(f"Книга {book_id} не знайдена в бібліотеці.")

    def update_book(self, book_id, title=None, author=None, year=None, genre=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                book["назва"] = title
            if author:
                book["автор"] = author
            if year:
                book["рік"] = year
            if genre:
                book["жанр"] = genre
            print(f"Інформація про книгу {book_id} оновлена.")
        else:
            print(f"Книга {book_id} не знайдена в бібліотеці.")

library = Library()
library.books = {
    1: {"назва": "Майстер і Маргарита", "автор": "Михайло Булгаков", "рік": 1966, "жанр": "фантастика"},
    2: {"назва": "1984", "автор": "Джордж Орвелл", "рік": 1949, "жанр": "антиутопія"},
    3: {"назва": "Гра престолів", "автор": "Джордж Р. Р. Мартін", "рік": 1996, "жанр": "фентезі"}
}

while True:
    print("\nМеню опцій:")
    print("1. Показати бібліотеку")
    print("2. Додати нову книгу")
    print("3. Видалити книгу")
    print("4. Оновити інформацію про книгу")
    print("5. Вийти")

    choice = input("Виберіть опцію (1-5): ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book_id = int(input("Введіть ідентифікатор книги: "))
        title = input("Введіть назву книги: ")
        author = input("Введіть автора книги: ")
        year = int(input("Введіть рік видання: "))
        genre = input("Введіть жанр книги: ")
        library.add_book(book_id, title, author, year, genre)
    elif choice == "3":
        book_id = int(input("Введіть ідентифікатор книги для видалення: "))
        library.delete_book(book_id)
    elif choice == "4":
        book_id = int(input("Введіть ідентифікатор книги для оновлення: "))
        title = input("Нова назва книги (натисніть Enter, якщо не потрібно змінювати): ")
        author = input("Новий автор книги (натисніть Enter, якщо не потрібно змінювати): ")
        year = input("Новий рік видання (натисніть Enter, якщо не потрібно змінювати): ")
        genre = input("Новий жанр книги (натисніть Enter, якщо не потрібно змінювати): ")

        if year:
            year = int(year)

        library.update_book(book_id, title, author, year, genre)
    elif choice == "5":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
