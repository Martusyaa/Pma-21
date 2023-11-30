class ArrayList:
    def __init__(self):
        self.array = []

    def add(self, element):
        if len(self.array) == self.capacity():
            self.resize()
        self.array.append(element)

    def remove(self, element):
        try:
            self.array.remove(element)
        except ValueError:
            print(f"{element} not found in the list")

    def remove_at(self, index):
        try:
            if index < 0 or index >= len(self.array):
                raise IndexError("Index out of range")
            del self.array[index]
        except IndexError as e:
            print(e)

    def insert(self, index=None, element=None):
        try:
            if index is None:
                index = len(self.array)
            elif index < 0 or index > len(self.array):
                raise IndexError("Index out of range")

            if element is None:
                raise ValueError("Element cannot be None")

            if len(self.array) == self.capacity():
                self.resize()
            self.array.insert(index, element)
        except (IndexError, ValueError) as e:
            print(e)

    def clear(self):
        self.array = []

    def capacity(self):
        return int(1.5 * len(self.array) + 1)

    def resize(self):
        new_capacity = int(1.5 * len(self.array) + 1)
        new_array = [None] * new_capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array


my_list = ArrayList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)


print("Original List:", my_list.array)

my_list.remove(2)
print("List after removing 2:", my_list.array)

my_list.remove(5)

my_list.insert(1, 5)
print("List after inserting 5 at index 1:", my_list.array)
my_list.insert(1, 15)
print("List after inserting 5 at index 1:", my_list.array)
my_list.insert(1, 25)
print("List after inserting 5 at index 1:", my_list.array)
my_list.insert(1, 35)
print("List after inserting 5 at index 1:", my_list.array)

my_list.insert(10, 7)

my_list.insert(element=8)
print("List after inserting 8 without index:", my_list.array)

my_list.remove_at(2)
print("List after removing at index 2:", my_list.array)

my_list.clear()
print("List after clearing:", my_list.array)
