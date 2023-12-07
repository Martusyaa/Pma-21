from agregator import capacity_agregator
class ArrayList:
    def __init__(self):
        self.capacity = 10
        self.elements = [None] * self.capacity
        self.size = 0

    @capacity_agregator
    def add(self, element):
        self.elements[self.size] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        removed_element = self.elements[index]
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        self.size -= 1
        return removed_element

    @capacity_agregator
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = element
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.elements[index]

    def clear(self):
        self.elements = [None] * self.capacity
        self.size = 0

    def _increase_capacity(self):
        new_capacity = int(self.capacity * 1.5) + 1
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
