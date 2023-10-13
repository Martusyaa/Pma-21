class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity

    def add(self, element):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = element
        self.size += 1

    def remove(self, element):
        if element in self.array:
            index = self.array.index(element)
            self._shift_left(index)
            self.size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize()
        self._shift_right(index)
        self.array[index] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self):
        self.capacity = int(1.5 * self.capacity) + 1
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def _shift_left(self, index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None

    def _shift_right(self, index):
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, element):
        new_node = Node(element)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, element):
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


def read_array_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]


def read_list_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]


def write_list_to_file(filename, linked_list):
    with open(filename, 'w') as file:
        current = linked_list.head
        while current:
            file.write(str(current.data) + '\n')
            current = current.next


def write_array_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')


def main():
    array_list = ArrayList()
    linked_list = LinkedList()


    array_data = read_array_from_file('array_data.txt')
    linked_data = read_list_from_file('linked_data.txt')

    for element in array_data:
        array_list.add(element)

    for element in linked_data:
        linked_list.add(element)
    linked_list.add(1)
    linked_list.add(6)
    print(linked_list)

    array_list.add(66)
    linked_list.remove(7)
    array_list.insert(array_list.size, 9)
    # linked_list.clear()

    write_array_to_file('array_result.txt', array_list.array[:array_list.size])
    write_list_to_file('linked_result.txt', linked_list)


if __name__ == "__main__":
    main()
