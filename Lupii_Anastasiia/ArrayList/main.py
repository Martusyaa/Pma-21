
class ArrayList:
    CAPACITY = 10

    def __init__(self, array=None):
        if array is None:
            array = []
        self.size = len(array)
        self.capacity = max(ArrayList.CAPACITY, self.size)
        self.capacity = int(1.5 * self.capacity) + 1
        self.array = [None] * self.capacity
        for i in range(self.size):
            self.array[i] = array[i]

    def add(self, element):
        if self.size == self.capacity:
            self._expand()

        self.array[self.size] = element
        self.size += 1

    def remove(self, element):
        index = self.array.index(element)
        if index != -1:
            self._remove_at(index)

    def _remove_at(self, index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def insert(self, index, element):
        try:
            if index < 0 or index > self.size:
                raise IndexError("Invalid index")

            if self.size == self.capacity:
                self._expand()

            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]

            self.array[index] = element
            self.size += 1
        except IndexError as e:
            print(e)

    def clear(self):
        self.size = 0
        self.array = [0] * self.capacity

    def _expand(self):
        print(f"Size before expanding: {self.capacity}")

        new_capacity = int(1.5 * self.capacity) + 1
        new_array = [0] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

        print(f"Size after expanding: {self.capacity}")


my_list = ArrayList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
print("Origin array:", my_list.array)

my_list.add(10)
print("after adding element:", my_list.array)

my_list.remove(5)
print("deleting element:", my_list.array)

my_list.insert(0, 99)
print("after inserting element by index:", my_list.array)

my_list.clear()
print("After clearing:", my_list.array)
