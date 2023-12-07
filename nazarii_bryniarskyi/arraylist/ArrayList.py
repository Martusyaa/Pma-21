class ArrayList:

    def __init__(self, array=None):
        if array is None:
            self.arr = []
            self.capacity = 10
            self.current_index = 0
        else:
            self.arr = array
            self.capacity = int(len(array) * 1.5) + 1
            self.current_index = len(arr)


    def add(self, element, index=None):
        if index is None:
            if self.current_index+1 == self.capacity:
                self.capacity = int(len(self.arr) * 1.5) + 1
            self.arr.append(element)
            self.current_index += 1
        else:
            if index > self.current_index:
                raise IndexError
            else:
                if index >= self.capacity:
                    self.arr.extend([0] * (index - len(self.arr) + 1))
                for i in range(len(self.arr) - 1, index, -1):
                    self.arr[i] = self.arr[i - 1]
                self.arr[index] = element
                self.current_index += 1


    def get(self, index):
        if 0 <= index < self.current_index:
            return self.arr[index]
        else:
            raise IndexError


    def size(self):
        return self.current_index


    def clear(self):
        self.arr.clear()
        self.arr = [0] * 10
        self.current_index = 0


    def remove(self, index):
        if 0 <= index < self.current_index:
            for i in range(index, self.current_index - 1):
                self.arr[i] = self.arr[i + 1]
            self.current_index -= 1
        else:
            raise IndexError


    def __str__(self):
        return f"{self.arr[:self.current_index]}"



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    list = ArrayList(arr)
    list.add(11)
    list.add(99, 5)

    print(list)
