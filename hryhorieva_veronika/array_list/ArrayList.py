import sys

class ArrayList:
    def __init__(self, initial_list: list):
        self.array_list = [i for i in initial_list]
        self.maximum_size = len(self.array_list)+1
        self.current_size = len(self.array_list)
        self.index = len(self.array_list)-1

    def add(self, data):
        self.index += 1
        self.current_size += 1
        if self.maximum_size == self.current_size:
            self.refactor()
        self.array_list[self.index]=data



    def refactor(self):
        new_maximum_size = round((self.maximum_size * 1.5) + 1)
        new_list = [None] * new_maximum_size
        for i in range(len(self.array_list)):
            new_list[i] = self.array_list[i]
        self.array_list = new_list
        self.maximum_size = new_maximum_size

    def pop(self, index):
        try:
            if index < 0 or index >= self.current_size:
                raise Exception
            del self.array_list[index]
            self.current_size -= 1
            self.index-=1
        except Exception:
            print(f"Try to enter an index between 0 and {self.current_size - 1}")
            sys.exit(1)

    def insert(self, index, data):
        try:
            if index < 0 or index > self.current_size:
                raise Exception
            self.array_list.insert(index, data)
            self.current_size += 1
        except Exception:
            print(f"Try to enter index between 0 - {self.current_size}")
            sys.exit(1)

    def print(self):
        for item in self.array_list:
            print(item)



array_list = ArrayList([1, 2])
array_list.print()
# print("\n")
# array_list.print()
print("\n")
array_list.add(None)
array_list.add(26)

array_list.print()