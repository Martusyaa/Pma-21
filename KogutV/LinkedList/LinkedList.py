from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at(self, data, index):
        if index < 0:
            raise IndexError("Index can not be less than zero")
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            i = 0
            while current and i < index - 1:
                current = current.next
                i += 1
            if not current:
                raise IndexError("Index is out of bounds")
            
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def remove_at(self, index):
        if index < 0:
            raise IndexError("Index can not be less than zero")
        
        if index == 0:
            if not self.head:
                raise IndexError("Index is out of bounds")
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current = self.head
            i = 0
            while current and i < index:
                current = current.next
                i += 1
            if not current:
                raise IndexError("Index is out of bounds")
            
            if current == self.tail:
                self.tail = current.prev
                self.tail.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

    def clear(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")