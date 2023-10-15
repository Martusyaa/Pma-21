import sys


class Node:
    def __init__(self, data, next_e=None, previous_e=None):
        self.data = data
        self.previous_e = previous_e
        self.next_e = next_e

    def __del__(self):
        pass


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        # try catch must be not if OutOfRange
        if self.root is None:
            self.root = new_node
            return
        cur = self.root
        while cur.next_e:
            previous_temp = cur
            cur = cur.next_e  # перехід на некст
            cur.previous_e = previous_temp
        cur.next_e = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def remove(self, index: int):
        try:
            if index < 0 or index > self.size:
                raise IndexError
            previous = index - 1


            if index == 0:
                self.root = self.root.next_e
                self.size -= 1
                return

            cur = self.root
            counterfeit_index = 0
            while cur:
                if counterfeit_index == index:
                    prev_node = cur.previous_e
                    next_node = cur.next_e
                    if cur.next_e is not None:
                        prev_node.next_e = next_node
                    if cur.previous_e is not None:
                        next_node.previous_e = cur.previous_e
                    self.size -= 1
                    return
                cur = cur.next_e
                counterfeit_index += 1
        except IndexError:
            print("Index not in range!")
            sys.exit(1)

    def __str__(self):
        cur = self.root
        result = ""
        while cur:
            if cur == self.root:
                result += str(cur.data) + " -> "
                cur = cur.next_e
            else:
                if cur.next_e is None:
                    result += str(cur.data)
                    break
                else:
                    result += str(cur.data) + " -> "
                    cur = cur.next_e
        return result


linked_list = LinkedList()
linked_list.add(0)
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
linked_list.add(6)
linked_list.add(7)
linked_list.add(8)
linked_list.add(9)
linked_list.add(10)
print(linked_list)
linked_list.remove(5)
linked_list.remove(0)
linked_list.remove(1)

print(linked_list)

