from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# BOOKS = None
BOOKS = {
    '1': {
        'title': 'Murder on the Orient Express',
        'author': 'Agatha Christie',
        'publication year': 1934,
        'genre': 'mystery'
    },
    '2': {
        'title': 'The Count of Monte Cristo',
        'author': 'Alexandre Dumas',
        'publication year': 1844,
        'genre': 'adventure'
    },
    '3': {
        'title': 'The Lion, the Witch and the Wardrobe',
        'author': 'C.S. Lewis',
        'publication year': 1950,
        'genre': 'fantasy'
    }
}

parser = reqparse.RequestParser()
class BooksList(Resource):
    def get(self):
        return BOOKS

    def post(self):
        if BOOKS == None:
            return "List book is none.", 404
        parser.add_argument("title")
        parser.add_argument("author")
        parser.add_argument("publication year")
        parser.add_argument("genre")
        args = parser.parse_args()

        book_id = str(int(max(BOOKS.keys())) + 1)
        BOOKS[book_id] = {
            "title": args["title"],
            "author": args["author"],
            "publication year": args["publication year"],
            "genre": args["genre"],
        }
        return BOOKS[book_id], 201

class Book(Resource):
    def get(self, book_id):
        if book_id not in BOOKS:
            return "Not found", 404
        else:
            return BOOKS[book_id]
    def patch(self, book_id):
        parser.add_argument("title")
        parser.add_argument("author")
        parser.add_argument("publication year")
        parser.add_argument("genre")
        args = parser.parse_args()
        if book_id not in BOOKS:
            return "Record not found", 404
        else:
            book = BOOKS[book_id]
            book["title"] = args["title"] if args["title"] is not None else book["title"]
            book["author"] = args["author"] if args["author"] is not None else book["author"]
            book["publication year"] = args["publication year"] if args["publication year"] is not None else book["publication year"]
            book["genre"] = args["genre"] if args["genre"] is not None else book["genre"]
            return book, 200

    def delete(self, book_id):
        if book_id not in BOOKS:
            return "Not found", 404
        else:
            del BOOKS[book_id]
            return '', 204


api.add_resource(BooksList, '/books/')
api.add_resource(Book, '/books/<book_id>')

if __name__ == "__main__":
    app.run(debug=True)

# ?title=And Then There Were None&author=Agatha Christie&publication year=1939&genre=mystery
# ?author=Agatha Mary Clarissa Christie