class ArrayList:
    CAPACITY = 5

    def __init__(self, array=None):
        self.array = list(array) if array else []
        self.capacity = max(ArrayList.CAPACITY, len(self.array))

    def expand(self):
        new_capacity = int(1.5 * self.size) + 1
        self.capacity = max(new_capacity, ArrayList.CAPACITY)
        self.array += [0] * (self.capacity - len(self.array))

    def add_element(self, element):
        if len(self.array) == self.capacity:
            self.expand()
        self.array.append(element)

    def delete_element(self, index=None):
        if not self.array:
            raise ValueError("Can't delete, the array is empty")

        index = index if index is not None else len(self.array) - 1

        if 0 <= index < len(self.array):
            print("After delete:")
            del self.array[index]

    def add_index(self, index, element):
        if 0 <= index <= len(self.array):
            if len(self.array) == self.capacity:
                self.expand()
            print("After add:")
            self.array.insert(index, element)

    def clear(self):
        if not self.array:
            raise ValueError("Can't clear, the array is empty")

        print("After clear")
        self.array.clear()

    def print_array(self):
        print(self.array)


import random

if __name__ == '__main__':
    array = ArrayList([5, 3, 4, 5])

    array.print_array()
    array.add_element(2)
    array.print_array()

    array.delete_element()
    array.print_array()

    array.add_index(1, 13)
    array.print_array()

    array.clear()

    array.print_array()