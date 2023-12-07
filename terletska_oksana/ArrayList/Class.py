class ArrayList:
    CAPACITY = 1

    def __init__(self, array=None):
        if array is None:
            array = []
        self.size = len(array)
        self.capacity = max(ArrayList.CAPACITY, self.size)
        self.array = [0] * self.capacity
        for i in range(self.size):
            self.array[i] = array[i]

    def __str__(self):
        if self.is_empty():
            return "[] is empty"
        return str(self.array[:self.size])

    def is_empty(self):
        return self.size == 0

    def resize(self, new_capacity):
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, element):
        if self.size == self.capacity:
            if self.is_empty():
                self.resize(ArrayList.CAPACITY)
            else:
                self.resize(int(1.5 * self.capacity) + 1)
        self.array[self.size] = element
        self.size += 1
        print("New capacity:", self.capacity)

    def remove(self, index=0):
        if self.is_empty():
            print("ArrayList is empty, unable to remove.")
            return
        if index < 0 or index >= self.size:
            print("Index not found, unable to remove.")
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            print("Index not found")
            return
        if self.size == self.capacity:
            self.resize(int(1.5 * self.capacity) + 1)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.capacity = ArrayList.CAPACITY
        self.array = [0] * self.capacity
