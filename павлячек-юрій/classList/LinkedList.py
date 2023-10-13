class LinkedList:

    def __init__(self, linked_list=None):
        self.INVALID_INDEX = 'Invalid index'
        self.first = None
        if linked_list is not None:
            self.first = linked_list.first

    class _Node:
        def __init__(self, previous, element, next):
            self.previous = previous
            self.element = element
            self.next = next

    def add(self, element, index=None):
        if index is None:
            if self.first is None:
                self.first = self._Node(None, element, None)
            else:
                self.first.next = self._Node(self.first, element, None)
                self.first = self.first.next
        else:
            if index < 0 or index > self.size():
                raise ValueError(self.INVALID_INDEX)

            if self.size() < 1:
                new_node = self._Node(None, element, self.first)
                self.first = new_node
            else:
                temp = self.first
                for i in range(self.size() - index - 1):
                    temp = temp.previous
                new_node = self._Node(temp.previous, element, temp)
                if index != 0:
                    temp.previous.next = new_node
                temp.previous = new_node

    def print(self, index):
        if index >= self.size() or index < 0:
            raise ValueError(self.INVALID_INDEX)

        temp = self.first
        element = temp.element

        for i in range(self.size() - index):
            element = temp.element
            temp = temp.previous

        return element

    def pop(self, index):
        if index < 0 or index >= self.size():
            raise ValueError(self.INVALID_INDEX)

        temp = self.first
        for i in range(self.size() - index - 1):
            temp = temp.previous
        if index != 0:
            temp.previous.next = temp.next
        if temp.next is not None:
            temp.next.previous = temp.previous

    def size(self):
        size = 0
        temp = self.first

        while temp is not None:
            size += 1
            temp = temp.previous

        return size

    def clear(self):
        self.first = None
