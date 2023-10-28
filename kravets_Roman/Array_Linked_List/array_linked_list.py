class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class ArrayList:
    def __init__(self, array=[]):
        self.capacity = 5
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = int(1.5 * self.capacity) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, item):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = item
        self.size += 1

    def remove(self, item):
        if item in self.array:
            index = self.array.index(item)
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1

    def insert(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.size += 1

    def clear(self):
        self.size = 0
        self.array = [None] * self.capacity


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, item):
        current = self.head
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insert(self, index, item):
        if index < 0:
            raise IndexError("Index out of bounds")
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                if current is None:
                    raise IndexError("Index out of bounds")
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            else:
                self.head = new_node
            current.prev = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"


arr_list = ArrayList()
arr_list.add(1)
arr_list.add(2)
arr_list.add(3)
arr_list.add(7)
arr_list.add(6)
print(arr_list.array)
arr_list.remove(2)
print(arr_list.array)
arr_list.insert(3, 2)
print(arr_list.array)

ll = LinkedList()
ll.add(1)
ll.add(3)
ll.add(7)
ll.add(2)
ll.remove(2)
ll.insert(1, 4)
print(ll)
