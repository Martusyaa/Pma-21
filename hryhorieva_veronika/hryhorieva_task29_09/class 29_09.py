from itertools import cycle
class Chips:
    def __init__(self, taste, price=0):
        self.taste = taste
        self.price = price



chips_crab = Chips("crab", 25)
chips_cheese = Chips("cheese", 12)
chips_cucumber = Chips("cucumber", 5)

list_of_chips = []
list_of_chips.append(chips_crab)
list_of_chips.append(chips_cheese)
list_of_chips.append(chips_cucumber)

# print(l)

catalog_of_prices = []
for chips in range(len(list_of_chips)):
    catalog_of_prices.append(list_of_chips[chips].price)

print("Prices of chips: ")
for i in range(len(list_of_chips)):
    print(list_of_chips[i].price)
list_of_chips_stream = cycle(list_of_chips)



inflation_prices = list(map(lambda chips: chips.price ** 2, list_of_chips))

print("Prices after the inflation: ")
list_of_chips_stream = cycle(inflation_prices)
for _ in range(len(list_of_chips)):
    chip = next(list_of_chips_stream)
    print(chip)
