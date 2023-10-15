class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert_head(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def delete_head(self):
        if self.isEmpty():
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def insert_tail(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.insert_head(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.previous = current

    def delete_tail(self):
        if self.isEmpty():
            print("list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.previous.next = None
            current.previous = None

    def insert_position(self, data, position):
        current = self.head
        count = 1
        while current is not None:
            if count == position - 1:
                break
            count += 1
            current = current.next
        if position == 1:
            self.insert_head(data)
        elif current is None:
            print("cant to insert")
        elif current.next is None:
            self.insert_tail(data)
        else:
            new_node = Node(data)
            new_node.next = current.next
            new_node.previous = current
            current.previous = new_node
            current.next = new_node
            current.next.previous = new_node

    def delete_position(self, position):
        if self.isEmpty():
            print("List is empty.")
        elif position == 1:
            self.delete_head()
        else:
            current = self.head
            count = 1
            while current is not None:
                if count == position:
                    current.previous.next = current.next
                    if current.next:
                        current.next.previous = current.previous
                    current.next = None
                    current.previous = None
                    break
                current = current.next
                count += 1
            if current is None:
                print("cant delete")

    def display_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def deleteAll(self):
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = None
            current.previous = None
            current = next_node
        self.head = None