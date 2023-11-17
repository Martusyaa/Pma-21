class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.head = None
        if array is not None:
            for element in array:
                self.append(element)

    def push(self, NewVal):
        try:
            NewNode = Node(NewVal)
            NewNode.next = self.head
            if self.head is not None:
                self.head.prev = NewNode
            self.head = NewNode
        except TypeError:
            print("Неправильний тип")

    def insert(self, prev_node, NewVal):

        if prev_node is None:
            raise ValueError("Попередній вузол не може бути 0")
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def append(self, NewVal):
        try:
            NewNode = Node(NewVal)
            NewNode.next = None
            if self.head is None:
                NewNode.prev = None
                self.head = NewNode
                return
            last = self.head
            while (last.next is not None):
                last = last.next
            last.next = NewNode
            NewNode.prev = last
            return
        except TypeError:
            print("Неправильний тип")
        except NameError:
            print("name error")

    def listprint(self, node):
        try:
            while (node is not None):
                print(node.data),
                last = node
                node = node.next

        except AttributeError:
            print("Вивід даних з пустого списку")

    def clear(self):
        try:
            current = self.head
            while current:
                next_node = current.next
                current.prev = None
                current.next = None
                current = next_node
            self.head = None
        except Exception as e:
            print(f"An error occurred: {str(e)}")


dllist = DoublyLinkedList([])
dllist.push(4)
dllist.append(5)
dllist.push(8)
dllist.push(3)
dllist.insert(dllist.head.next.next, 13)
dllist.append(45)
# dllist.clear()
dllist.listprint(dllist.head)
