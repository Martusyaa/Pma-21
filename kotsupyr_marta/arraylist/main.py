ERROR = "Index out of range."
NUMBER = 4
class ArrayList:
    def __init__(self, array = []):
        self.len = NUMBER
        self.size = len(array)
        self.array = array
        if len(self.array) > 0:
            self.resise()
        else:
            self.array = [None] * self.len

    def __str__(self):
        # return str([x for x in self.array[:self.size] if x is not None])
        return str([x for x in self.array[:self.size]])

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

    def reverse(self):
        self.array.reverse()

    def clean(self):
        self.size = 0
        self.array = [None] * self.len
