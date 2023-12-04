class Library:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car: {self.brand}, Model: {self.model}, Year: {self.year}"


Car = {
        "Car1": Library("Toyota", "Camry", "2022"),
        "Car2": Library("Dodge", "Charger", "2019")
}

print("Даний словник:")
for key in Car:
    print(key, Car[key])

print("Словник після видалення елементу:")
key = "Car2"
try:
    del Car[key]
except KeyError:
    print(f"Ключ '{key}' не знайдено в словнику.")
else:
    for key in Car:
        print(key, Car[key])

print("Словник після заміни Car:")

new_car = Library("Toyota", "Corolla", 2023)
key = 'Car1'
try:
    if key in Car:
        Car[key] = new_car
        for key in Car:
            print(key, Car[key])
    else:
        raise KeyError(f"Ключ '{key}' не знайдено в словнику")
except KeyError as e:
    print(f"Error: {e}")
