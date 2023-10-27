from Class import Library
if __name__ == '__main__':

    Books = {
        "Book_first": Library("Paper towns", "John Green", "400"),
        "Book_second": Library("I say no", "Wilkie Collins", "350"),
        "Book_third": Library("The fault in our stars", "John Green", "340")
        }

print("Даний словник:")
for key in Books:
    print(key, Books[key])

print("Словник після видалення елементу:")
key = "Book_first"
try:
    del Books[key]
except KeyError:
    print(f"Ключ '{key}' не знайдено в словнику.")
else:
    for key in Books:
        print(key, Books[key])

print("Словник після заміни книги:")
new_book = Library("Kobzar", "Taras Shevchenko", 390)
key = 'Book_third'
try:
    if key in Books:
        Books[key] = new_book
        for key in Books:
            print(key, Books[key])
    else:
        raise KeyError(f"Ключ '{key}' не знайдено в словнику")
except KeyError as e:
    print(f"Error: {e}")