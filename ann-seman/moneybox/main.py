import constants
import os


class FileIsEmpty(Exception):

    def __init__(self, message="Файл пустий!"):
        self.message = message
        super().__init__(self.message)


class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, coin):
        if self.capacity >= coin:
            return True
        else:
            return False

    def add(self, coin):
        if self.can_add(coin):
            self.money += coin
            return True
        else:
            return False


try:
    with open(constants.INPUT_FILE, 'r') as file:
        if os.path.getsize(constants.INPUT_FILE) == 0:
            raise FileIsEmpty

        lines = file.readlines()
        capacity = int(lines[0])
        money_in_box = int(lines[1])
        add_to_box = int(lines[2])
        box = MoneyBox(capacity)

        if not box.add(money_in_box):
            print("False")
        if box.add(add_to_box):
            print("True")
        else:
            print("False")
except FileIsEmpty as e:
    print(e)
