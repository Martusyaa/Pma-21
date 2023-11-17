class FilmDictionary:
    def __init__(self, title, year, director):
        self.title = title;
        self.year = year
        self.director = director

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}, Director: {self.director}"

films = {"Interstaller":FilmDictionary('Інтерстеллар', 2014, 'Крістофер Нолан'),
         "Matrix":FilmDictionary('Матриця', 1999, 'Лана та Лілі Вачовскі'),
         "Green mile":FilmDictionary('Зелена миля', 1999, 'Френк Дарабонт'),
         "Toy Story":FilmDictionary("Історія іграшок", 1995, "Джон Лассетер")}

films.pop("Matrix")

new_films = FilmDictionary("Румунська печера", 2023, "Молдован")
films["Romanian cave"] = new_films

for i in films.values():
    print(i)
print()

films["Romanian cave"] = FilmDictionary("Румунська печера", 1999, "Румун")

films["Toy Story"].year = 1975

for i in films.values():
    print(i)
print()