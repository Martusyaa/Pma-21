class ArrayList:
    CAPACITY = 5
    def __init__(self, array=None):
        if array is None:
            array = []
        self.size = len(array)
        self.capacity = max(ArrayList.CAPACITY, self.size)
        print("Нова ємність: ", self.capacity )
        self.array = [0] * self.capacity
        for i in range(self.size):
            self.array[i] = array[i]


    def expansion(self):
        new_capacity = int(1.5 * self.size) + 1
        new_array = [0] * new_capacity
        print(f"Ємність масиву збільшилась до {new_capacity}")

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def add_element(self, element):
        if self.size == len(self.array):
            self.expansion()

        self.array[self.size] = element
        self.size += 1

    def print_array(self):
        print(f"{self.array}")

    def delete_element(self, index=None):
        if self.size == 0:
            raise ValueError("Неможливе видалення елемента, тому що масив пустий")

        if index is None:
            index = self.size - 1  # Видаляємо останній елемент за замовчуванням

        if index < 0 or index >= self.size:
            raise ValueError("Неприпустимий індекс для видалення елемента")

        print("Масив після видалення елемента:")
        new_array = [0] * self.capacity

        for i in range(index):
            new_array[i] = self.array[i]

        for i in range(index + 1, self.size):
            new_array[i - 1] = self.array[i]

        self.size -= 1
        self.array = new_array

    def add_index(self, index, element):
        if index < 0 or index > self.size:
            raise ValueError("Неприпустимий індекс")

        if self.size == len(self.array):
            self.expansion()

        print("Масив після додавання елемента по індексу: ")
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = element
        self.size += 1

    def clear(self):
        if self.size==0:
            raise ValueError("Неможливо очистити масив, тому що він пустий")

        print("Масив після очищення:")
        self.array=[]