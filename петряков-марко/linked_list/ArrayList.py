import sys


class ArrayList:
    def __init__(self, size=10):
        self.array_list = [None] * size
        self.maximum = size
        self.current_size = 0
        self.index = 0

    def add(self, data):
        if self.maximum_size == self.current_size:
            self.refactor()
        self.array_list[self.index] = data
        self.current_size += 1
        self.index += 1

    def refactor(self):
        new_maximum_size = round((self.maximum_size * 1.5) + 1)
        new_list = [None] * new_maximum_size
        for i in range(len(self.array_list)):
            new_list[i] = self.array_list[i]
        self.array_list = None
        self.maximum_size = new_maximum_size
        self.array_list = new_list

    def pop(self, index):
        try:
            if index < 0:
                raise Exception
            for i in range(index, len(self.array_list) - 1):
                self.array_list[i] = self.array_list[i + 1]
            self.current_size -= 1
        except IndexError:
            print(f"Try to enter index between 0 - {self.current_size}")
            sys.exit(1)
        except Exception as b:
            print(f"Try to enter index between 0 - {self.current_size}")
            sys.exit(1)

    def insert(self, index: int, data: int):
        new_l = self.array_list[:index]
        new_l += [data]
        new_l += self.array_list[index:]
        self.array_list = new_l
        self.current_size += 1

    def print(self):
        for i in self.array_list:
            print(i)


a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(10)
a.add(11)
a.pop(0)
a.pop(0)
a.pop(0)
a.pop(0)
a.print()
