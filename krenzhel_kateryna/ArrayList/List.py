ERROR = "Index out of range."

class ArrayList:
    def __init__(self, elements, array):
        self.len = elements
        self.size = len(array)
        self.array = array
        if len(self.array) > elements:
            self.resise()
        # self.array = [None] * self.len
        # self.array = [random.randint(1, 11) for i in range(elements)]

    def __str__(self):
        # return str([x for x in self.array[:self.size] if x is not None])
        return str([x for x in self.array[:self.size]])

    # def __str__(self):
    #     return "[" + ", ".join(str(x) if x is not None else "_" for x in self.array[:self.size]) + "]"
    #     # return "[" + ", ".join(str(x) if x is not None else ' ' for x in self.array[:self.size]) + "]"
    #     # return "[" + ", ".join(str(x) for x in self.array[:self.size] if x is not None) + "]"
    def print(self):
        print(self.array)
        print(self.__str__())
    def add(self, element):
        if self.size >= self.len:
            self.resise()
        self.array[self.size] = element
        self.size += 1

    def resise(self):
        new_len = int(1.5 * self.len + 1)
        new_array = [None] * new_len
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.len = new_len


    def insert(self, element, position):
        try:
            if self.size >= self.len:
                self.resise()
            for i in range(self.size, position, -1):
                self.array[i] = self.array[i - 1]
            self.array[position] = element
            self.size += 1
        except IndexError:
            print("Error: ", ERROR, '\n')

    def delete(self, element):
        self.array.pop(element)
        self.array.remove(element)

    def index(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                return i
        return None

    def pop(self, index):
        if index > self.size:
            print("Error: ", ERROR, '\n')
        else:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1

    def remove(self, element):
        index = self.index(element)
        if index is not None:
            self.pop(index)

    def clean(self):
        self.size = 0
        self.array = [None] * self.len
