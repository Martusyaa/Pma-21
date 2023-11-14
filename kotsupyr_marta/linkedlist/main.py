class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Недопустимий індекс")
        if index == self.size:
            self.add(data)
        else:
            new_node = Node(data)
            if index == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current = self.head
                for _ in range(index):
                    current = current.next
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            self.size += 1

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Недопустимий індекс")
        if self.size == 1:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        elif index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            removed_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removed_data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return removed_data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

my_linked_list = MyLinkedList()
my_linked_list.add(1)
my_linked_list.add(2)
my_linked_list.add(3)
print(my_linked_list.get_size())
my_linked_list.add_at(1, 4)
print(my_linked_list.remove_at(2))
my_linked_list.clear()
print(my_linked_list.is_empty())
