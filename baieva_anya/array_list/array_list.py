import sys


class ArrayList:
    def __init__(self, value_list:list):
        self.array_list = [i for i in value_list]
        self.maximum_size = len(value_list)+1
        self.current_size = len(self.array_list)
        self.index = len(self.array_list)-1


    def display(self):
        for i in range(self.current_size):
            print(self.array_list[i], end=" ")
        print()

    def add(self, data):
        self.current_size += 1
        self.index+=1
        if self.current_size == self.maximum_size:
            self._resize()
        self.array_list[self.index] = data


    def _resize(self):
        new_maximum_size = round(self.maximum_size * 1.5+1)
        new_list = [None] * new_maximum_size
        for i in range(self.current_size):
            new_list[i] = self.array_list[i]
        self.array_list = new_list
        self.maximum_size = new_maximum_size

    def pop(self, index):
        try:
            if index < 0 or index >= self.current_size:
                raise Exception
            del self.array_list[index]
            self.current_size -= 1
            self.index -= 1
        except Exception as e:
            print("OUT OF RANGE")


    def insert(self, index, data):
        try:
            if index < 0 or index > self.current_size:
                raise Exception
            self.array_list.insert(index,data)
            self.current_size+=1
        except Exception:
            print(f"Enter index betweeen 0 - {self.current_size}")
            sys.exit(1)




a = ArrayList([1,2,3,4,5,6,7,8,9,10])
a.display()
print("---------------------------")
a._resize()
a.add(83)
a.add(105)
# a.pop(0)
# a.pop(0)
# a.insert(3,234)

a.display()
print(a.maximum_size)