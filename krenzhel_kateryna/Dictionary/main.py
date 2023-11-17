ERROR = 'No book with this ID.'
books = {
    1: {
        'title': 'Murder on the Orient Express',
        'author': 'Agatha Christie',
        'publication year': 1934,
        'genre': 'mystery'
    },
    2: {
        'title': 'The Count of Monte Cristo',
        'author': 'Alexandre Dumas',
        'publication year': 1844,
        'genre': 'adventure'
    },
    3: {
        'title': 'The Lion, the Witch and the Wardrobe',
        'author': 'C.S. Lewis',
        'publication year': 1950,
        'genre': 'fantasy'
    }
}

def add_book(title, author, year, genre):
    new_id = max(books.keys()) + 1
    new_book = {
        'title': title,
        'author': author,
        'publication year': year,
        'genre': genre
    }
    books[new_id] = new_book
    print(f'Book with ID {new_id} has been added to the dictionary.')

def delete_book(book_id):
    if book_id in books:
        deleted_book = books.pop(book_id)
        print(f'Book "{deleted_book["title"]}" has been deleted from the dictionary.')
    else:
        # print('Error:', ValueError(ERROR))
        print(f'No book with ID {book_id} exists.')

def modify_book(book_id, field, new_value):
    if book_id in books and field in books[book_id]:
        books[book_id][field] = new_value
        print(f'Field "{field}" for book with ID {book_id} has been changed to "{new_value}".')
    else:
        # print('Error:', ValueError(ERROR))
        print(f'No book with ID {book_id} exists, or the field "{field}" does not exist.')

print("Initial dictionary of books:")
for book_id, book in books.items():
    print(f'Book ID: {book_id}, Book: {book}')

add_book('And Then There Were None', 'Agatha Christie', 1939, 'mystery')

modify_book(1, 'author', 'Agatha Mary Clarissa Christie')

delete_book(10)

print("Updated dictionary of books:")
for book_id, book in books.items():
    print(f'Book ID: {book_id}, Book: {book}')
