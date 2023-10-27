class ArrayList:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.size = len(array)
        self.capacity = self.size
        print("Нова ємність: ", self.capacity)
        self.array = [0] * self.capacity
        for i in range(self.size):
            self.array[i] = array[i]

    def add(self, element):
        if self.size == self.capacity:
            # Масив заповнений, потрібно розширити
            self._resize()
        self.array[self.size] = element
        self.size += 1

    def _resize(self):
        new_capacity = int(1.5 * self.capacity) + 1
        new_array = [None] * new_capacity
        print(f"Ємність масиву збільшилась до {new_capacity}")
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity
        self.array = new_array

    def delete_element(self, index=None):
        if index is None:
            index = self.size - 1

        new_array = [0] * self.capacity

        for i in range(index):
            new_array[i] = self.array[i]

        for i in range(index + 1, self.size):
            new_array[i - 1] = self.array[i]

        self.size -= 1
        self.array = new_array


    def insert(self, index, element):
        if 0 <= index <= self.size:
            raise ValueError("Неприпустимий індекс")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
            self.array[index] = element
            self.size += 1

    def clear(self):
        if self.size == 0:
            raise ValueError("Неможливо очистити масив, тому що він пустий")
        self.size = 0
        #self.array = [None] * self.capacity

    def print_array(self):
        if self.size == 0:
            print("Масив порожній.")
        else:
            for i in range(self.size):
                print(self.array[i], end=" ")
            print()

my_array = ArrayList([2, 4, 5, 1, 6, 4,2,3])
my_array.add(7)
my_array.print_array()

try:
    my_array.delete_element()
    print(my_array.delete_element())
except ValueError as e:
    print(e)

try:
    my_array.insert(9, 10)
    my_array.print_array()
except ValueError as e:
    print(e)

try:
    my_array.clear()
    my_array.print_array()
except ValueError as e:
    print(e)