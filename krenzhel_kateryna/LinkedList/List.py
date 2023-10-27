from Node import Node
ERROR = "Index out of range."

class LinkedList:
    def __init__(self, elements=[]):
        self.head = None
        self.tail = None
        for element in elements:
            self.append(element)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, data, index):
        new_node = Node(data)
        current = self.head
        count = 0
        try:
            while current:
                if count == index:
                    new_node.next = current
                    new_node.prev = current.prev
                    if current.prev:
                        current.prev.next = new_node
                    else:
                        self.head = new_node
                    current.prev = new_node
                    return
                count += 1
                current = current.next

            if count == index:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                return
            if count < index:
                raise IndexError(ERROR)
        except IndexError as e:
            print("Error: ", e)

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
