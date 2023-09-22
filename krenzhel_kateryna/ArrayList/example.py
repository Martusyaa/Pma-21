class ArrayList:
    def __init__(self):
        self.capacity = 10  # Початковий розмір масиву
        self.size = 0      # Поточний розмір списку
        self.data = [None] * self.capacity

    def __str__(self):
        return str(self.data[:self.size])

    def _resize(self):
        new_capacity = int(1.5 * self.capacity + 1)
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size >= self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove(self, value):
        index = self.index(value)
        if index is not None:
            self.pop(index)

    def pop(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def clear(self):
        self.capacity = 10
        self.size = 0
        self.data = [None] * self.capacity

    def index(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return None


# Приклад використання
arr_list = ArrayList()
arr_list.append(1)
arr_list.append(2)
arr_list.append(3)
print(arr_list)  # Виведе: [1, 2, 3]

arr_list.insert(1, 4)
print(arr_list)  # Виведе: [1, 4, 2, 3]

arr_list.remove(2)
print(arr_list)  # Виведе: [1, 4, 3]

arr_list.pop(0)
print(arr_list)  # Виведе: [4, 3]

arr_list.clear()
print(arr_list)  # Виведе: []
