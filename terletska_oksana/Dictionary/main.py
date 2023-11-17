from Class import Garden

plants = {
    "peony": Garden("flower", "pink", 1),
    "acacia": Garden("tree", "white", 30),
    "jasmine": Garden("shrub", "white", 2)
}
print("\n")

print("Словник Plants:")
for x, y in plants.items():
    print(x, y)

print("\n")


def add_plant(name, type_of_plant, color, height):
    try:
        if height <= 0:
            raise ValueError("Висота має бути > 0.")

        new_plant = Garden(type_of_plant, color, height)
        plants[name] = new_plant
        print(f"Рослину {name} додано до Plants.")
    except ValueError:
        print("Висота має бути > 0.")
    except Exception as e:
        print(f"Помилка: {e}")


def delete_plant(key):
    try:
        if key in plants:
            deleted = plants.pop(key)
            print(f"Рослину {key} видалено.")
        else:
            print(f"Рослини з ключем {key} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


def change_plant(name, key_of_value, new_value):
    try:
        if name in plants:
            plant = plants[name]

            if key_of_value == "height" and new_value <= 0:
                raise ValueError("Висота має бути > 0.")

            if key_of_value in plant.__dict__:
                if key_of_value == "type_of_plant":
                    plant.type_of_plant = new_value
                elif key_of_value == "color":
                    plant.color = new_value
                elif key_of_value == "height":
                    plant.height = new_value

                print(f"Внесені зміни у рослину {name} у значення {key_of_value}")
            else:
                print(f"Рослини з ключем {key_of_value} не знайдено.")
        else:
            print(f"Рослини з ключем {name} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


delete_plant("acacia")
for x, y in plants.items():
    print(x, y)
print("\n")

add_plant("oak", "tree", "brown", 10)
for x, y in plants.items():
    print(x, y)
print("\n")

change_plant("peony", "height", 0.5)
for x, y in plants.items():
    print(x, y)
