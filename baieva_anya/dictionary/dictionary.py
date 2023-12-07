
def print_information(bookshelf):
    print("\n|BOOKSHELF|\n")
    for key, value in bookshelf.items():
        print("------------------------")
        print(key,value)


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"


bookshelf = {
    "Romance": Book("Jane Eyre - Charlotte Bronte"),
    "Detective": Book("Adatha Chiristie - The A.B.C Crime") ,
    "Philosophy": Book("Discourses - Epictetus")
}
print_information(bookshelf)

# Delete
bookshelf.pop("Detective")
print_information(bookshelf)

# Add
bookshelf.__setitem__("Poetry",
                      ["The Odyssey - Homer, The Divine comedy - Dante Alighieri, Bright Dead Things - Ada Limon"])
print_information(bookshelf)

# Replace
bookshelf.__setitem__("Romance",
                      ["Jane Eyre - Charlotte Bronte, Anna Karenina - Lev Tolstoy, Eugene Onegin - Alexander Pushkin"])
print_information(bookshelf)


