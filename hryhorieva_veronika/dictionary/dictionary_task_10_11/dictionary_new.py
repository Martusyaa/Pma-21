from class_for_dict import *


def print_dict():
    for key, value in dictionary_brands.items():
        print(f'Item: {key, str(value)}')


def change_value(key: str, name: str):
    print("Element changed!")
    dictionary_brands[key] = Gadget(name)


dictionary_brands = {"Apple": Gadget("iPhone 15 Pro Max"),
                     "Samsung": Gadget("Galaxy 15"),
                     "Xiaomi": Gadget("miBand")
                     }
dictionary_brands.pop("Apple")
print_dict()
dictionary_brands["Nokia"] = Gadget("G42")
change_value("Samsung", "Galaxy 18")
print_dict()
