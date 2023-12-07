from class_for_dict import *


def print_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        print(key, value)
    print("\n")


def add_element_in_dict(dictionary: dict, key: str, list_element: list, ):
    try:
        assert bool(dictionary.get(key)) == False
        a = bool(dictionary.get(key))
        print("The element added!")
        dictionary[key] = list_element
        print_dictionary(dictionary)

    except AssertionError as b:
        print("The key already exist in your dictionary")


def change_element_in_dict(dictionary: dict, key: str, remove: str):
    try:
        assert bool(dictionary.get(key)) == True
        print("The element deleted!")
        dictionary[key].remove(remove)
        print_dictionary(dictionary)


    except AssertionError as b:
        print("No key in your dictionary")

    except ValueError:
        print("No element in your key")


def delete_key(dictionary: dict, key: str, remove_name: str):
    try:
        assert key in dictionary and isinstance(dictionary[key], (list, Gadget))
        if isinstance(dictionary[key], list):
            for item in dictionary[key]:
                if isinstance(item, Gadget) and item.name == remove_name:
                    dictionary[key].remove(item)
                    print("The element deleted!")
                    break
        elif isinstance(dictionary[key], Gadget) and dictionary[key].name == remove_name:
            del dictionary[key]
            print("The element deleted!")
        else:
            print("No element with the given name in the key.")

    except AssertionError as e:
        print("Error:", e)


dictionary_brands = {"Apple": Gadget("iPhone 15 Pro Max"),
                     "Samsung": Gadget("Galaxy 15"),
                     "Xiaomi": Gadget("miBand"),
                     "Nokia": ["3310", "g42"]
                     }

print("Old dictionary: ")
print_dictionary(dictionary_brands)
add_element_in_dict(dictionary_brands, "Philips", ["TV", "Processor"])
delete_key(dictionary_brands, "Apple", "iPhone 15 Pro Max")
print_dictionary(dictionary_brands)
