class Array_list:
    def __init__(self, arr=[], length=None):
        if arr == []:
            if length == None:
                raise ValueError
            else:
                self.len = length
                self.last_element_index = 0
                self.array = [None for i in range(self.len)]
        else:
            if length == None:
                self.len = len(list(arr))
                self.last_element_index = len(arr)
                self.array = arr
            elif length >= len(arr):
                self.len = length
                self.last_element_index = len(arr)
                self.array = arr
                for i in range(length - len(arr)):
                    self.array.append(None)

    def append(self, value):
        if self.last_element_index == len(self.array):
            old_len = self.len
            self.len = int(self.len * 1.5 + 1)
            new_array = self.array
            new_array.append(value)
            for i in range(self.len - (old_len - 1)):
                new_array.append(None)
            self.array = new_array
            self.last_element_index += 1
        else:
            self.array[self.last_element_index] = value
            self.last_element_index += 1

    def clear(self):
        self.array = [None for i in range(self.len)]
        self.last_element_index = 0

    def pop(self):
        if self.array[self.last_element_index - 1] == None:
            raise ValueError
        else:
            to_return = self.array[self.last_element_index - 1]
            self.array[self.last_element_index - 1] = None
            self.last_element_index -= 1
            return to_return

    def __len__(self):
        return self.len

    def __str__(self):
        str_array = []
        for i in range(self.last_element_index):
            str_array.append(self.array[i])
        return str(str_array)


arr = Array_list(arr=[10, 11, 12, 13, 14], length=10)
print(arr)
print(len(arr))
for i in range(5):
    arr.append(i)
print(f"Array: {arr}; Array length before extension: {len(arr)}")
arr.append(1)
print(f"Array after extension: {arr}; Array length after extension: {len(arr)}")
arr.pop()
arr.pop()
print(arr)
arr.clear()
print(arr)

