from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

class Book:
    def __init__(self, book_id, title, author, year, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre
        }

class BookAPI:
    def __init__(self):
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            with open("book.json", "r") as file:
                data = json.load(file)
                self.books = [Book(book["book_id"], book["title"], book["author"], book["year"], book["genre"]) for book in data]
        except FileNotFoundError:
            print("File not found")
            self.books = []

    def save_data(self):
        data_to_save = [book.to_dict() for book in self.books]
        with open("book.json", "w") as file:
            json.dump(data_to_save, file)

    def get_books(self):
        return [book.to_dict() for book in self.books]

    def create_book(self, data):
        book_id = random.randint(1, 10000)
        book = Book(book_id, data["title"], data["author"], data["year"], data["genre"])
        self.books.append(book)
        self.save_data()
        return book.to_dict()

    def update_book(self, book_id, data):
        book = self.find_book_by_id(book_id)
        if book is not None:
            if "title" in data:
                book.title = data["title"]
            if "author" in data:
                book.author = data["author"]
            if "year" in data:
                book.year = data["year"]
            if "genre" in data:
                book.genre = data["genre"]
            self.save_data()
            return book.to_dict()
        return None

    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book is not None:
            self.books = [b for b in self.books if b.book_id != book_id]
            self.save_data()
            return book.to_dict()
        return None

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

book_api = BookAPI()

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(book_api.get_books())

@app.route('/books', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        if "title" not in data or "author" not in data or "year" not in data or "genre" not in data:
            raise KeyError("Title, author, year, and genre are required fields")
        book = book_api.create_book(data)
        return jsonify(book)
    except (KeyError) as e:
        return jsonify({"message": str(e)}), 400

@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    data = request.get_json()
    updated_book = book_api.update_book(book_id, data)
    if updated_book is not None:
        return jsonify(updated_book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted_book = book_api.delete_book(book_id)
    if deleted_book is not None:
        return jsonify(deleted_book), 200
    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)