from ClassNode import Node
class LinkedList():
    def __init__(self, elements=[]):
        self.first = None
        self.last = None
        self.size = 0
        for element in elements:
            self.add_to_end(element)

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def add_to_start(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.size += 1

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError("Такого індексу не існує")

        new_node = Node(data)

        if index == 0:
            self.add_to_start(data)
        elif index == self.size:
            self.add_to_end(data)
        else:
            actual = self.first
            for i in range(index):
                actual = actual.next

            new_node.prev = actual.prev
            new_node.next = actual
            actual.prev.next = new_node
            actual.prev = new_node
            self.size += 1

    def delete(self, data):
        if self.first is None:
            raise ValueError("Список вже порожній, неможливо видалити елемент")
        else:
            actual = self.first
            while actual:
                if actual.data == data:
                    if actual.prev:
                        actual.prev.next = actual.next
                    else:
                        self.first = actual.next

                    if actual.next:
                        actual.next.prev = actual.prev
                    else:
                        self.last = actual.prev

                    return
                actual = actual.next
                self.size += 1

    def clear(self):
        if self.first is None:
            raise ValueError("Список вже порожній, його не можливо очистити")
        else:
            self.first = None
            self.last = None
            self.size = 0

    def show(self):
        elements = []
        actual = self.first
        while actual:
            elements.append(actual.data)
            actual = actual.next
        return elements
