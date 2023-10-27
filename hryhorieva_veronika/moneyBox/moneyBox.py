import sys


class MoneyBox:
    def __init__(self, capacity: int, coins: int, already_added=0):
        self.already_added = already_added
        try:
            self.coins = coins
            self.capacity = capacity
            assert self.coins >= 0 and self.capacity > 0
        except AssertionError as b:
            print("The number of coins should be positive integer!")

        self.add(self.coins)

    def can_add(self):
        try:
            self.already_added += self.coins

            assert self.already_added + self.coins <= self.capacity
        except AssertionError as b:
            print("The capacity is failed. You cannot add more coins")
            sys.exit(1)

    def add(self, coins):
        self.coins = coins
        if self.can_add():
            self.already_added += coins

    def __str__(self):
        return f"MoneyBox\nCurrent_coins: {self.already_added}\nCapacity: {self.capacity}"


a = MoneyBox(20, 10)
print(a)
a.add(50)
print(a)
