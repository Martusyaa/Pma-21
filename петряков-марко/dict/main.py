# Menu key-name|value-price
from Dish import Dish


def print_dict(dictionary: dict):
    print("Menu")
    for key, value in dictionary.items():
        print(f"Dish:{key} | Price:{value}")


menu_dict = {
    "carbonara": Dish(123),
    "lasagna": Dish(124),
    "dumplings": Dish(2343),
    "chicken_roll": Dish(42342342)}

# # Add element to dict
# menu_dict["tea"] = Dish(20)
# # Add dict to dict
# beverage_menu = {"gorilka": Dish(1111),
#                  "beer": Dish("beer"),
#                  "cocktail": Dish(999)}
# menu_dict.update(beverage_menu)
# print_dict(menu_dict)
##Printing
# print_dict(menu_dict)
##Changing
# print_dict(menu_dict)
# menu_dict["lasagna"] = Dish(5455)
# print_dict(menu_dict)
##Deleting
# print_dict(menu_dict)
# menu_dict.popitem()
# print_dict(menu_dict)
# menu_dict.pop("carbonara")
# print_dict(menu_dict)
