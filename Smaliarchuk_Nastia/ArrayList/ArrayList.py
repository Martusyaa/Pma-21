import re


class ArrayList:
    def __init__(self, size=1):
        self.max_size = size
        self.list = [None] * size
        self.size = 0

    def __str__(self):
        return str(self.list).replace(", None", "")

    def __len__(self):
        return self.size

    def add(self, *elements):
        for elem in elements:
            if self.size >= self.max_size:
                self.grow()
            self.list[self.size] = elem
            self.size += 1
        return self

    def __getitem__(self, index):
        index = self.validate_index(index)
        return self.list[index]

    def grow(self):
        new_max_size = self.max_size * 2
        new_list = [None] * new_max_size
        for index in range(self.size):
            new_list[index] = self.list[index]
        self.max_size = new_max_size
        self.list = new_list

    def validate_index(self, index):
        if index < 0:
            index = self.size + index
        if index < 0 or index > self.size:
            raise IndexError("ArrayList index out of range")
        return index

    def __delitem__(self, index):
        index = self.validate_index(index)
        for i in range(index, self.size):
            self.list[i] = self.list[i+1] if i < self.size - 1 else None
        self.size -= 1
        return self

    def delete(self, index):
        del self[index]
        return self

    def __iter__(self):
        for index in range(self.size):
            yield self.list[index]

    def count(self, to_count):
        count = 0
        for elem in self:
            if elem == to_count:
                count += 1
        return count

    def remove_entries(self, to_remove, entries=1):
        index = 0
        while index < self.size:
            if self[index] == to_remove:
                del self[index]
                entries -= 1
                if entries == 0:
                    break
            else:
                index += 1

        return self

    def remove_entries_all(self, *to_remove):
        index = 0
        while index < self.size:
            if self[index] in to_remove:
                del self[index]
            else:
                index += 1

        return self

    def __contains__(self, value):
        for elem in self:
            if elem == value:
                return True
        return False

    def __setitem__(self, index, value):
        index = self.validate_index(index)
        self.list[index] = value

    def reverse(self):
        for index in range(self.size//2):
            self.list[index], self.list[self.size-index - 1] =\
                self.list[self.size-index-1], self.list[index]
        return self

    def clear(self):
        self.size = 0
        self.max_size = 1
        self.list = [None]
        return self

    def pop(self):
        popped = self[-1]
        del self[-1]
        return popped

    def insert(self, index, *elements):
        index = self.validate_index(index)
        to_add = ArrayList(self.size-index)
        for i in range(index, self.size):
            to_add.add(self.list[i])
        self.size = index
        self.add(*elements)
        self.add(*to_add)
        return self
