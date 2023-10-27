class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev


class Linked_List:
    def __init__(self, elements=None):
        self.head = None
        if elements is not None:
            self.create_list(elements)

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [\n' + str(current.data) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.data) + '\n'
            return out + ']'
        return 'LinkedList []'

    def create_list(self, elements):
        for data in elements:
            self.append(data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_Node = self.head
            while curr_Node.get_next() is not None:
                curr_Node = curr_Node.get_next()
            new_node.set_prev(curr_Node)
            curr_Node.set_next(new_node)

    def show_List(self):
        if self.head is None:
            print("The list is empty.")
        else:
            curr_Node = self.head
            while curr_Node != None:
                print(curr_Node.get_data())
                curr_Node = curr_Node.get_next()

    def list_lenght(self):
        if self.head is None:
            print("The list is empty.")
            return 0
        else:
            curr_Node = self.head
            counter = 0
        while curr_Node != None:
            counter += 1
            curr_Node = curr_Node.get_next()
        return counter

    def push_front(self, data):
        new_Node = Node(data)
        curr_Node = self.head
        new_Node.set_next(curr_Node)
        self.head = new_Node

    # def remove_first(self):
    #     if self.head is None:
    #         print("The list is empty.")
    #     else:
    #         curr_Node = self.head
    #         self.head = curr_Node.set_next()
    def searching_Element(self, data):
        curr_Node = self.head
        counter = 0
        while curr_Node is not None:
            if curr_Node.data == data:
                return counter
            counter += 1
            curr_Node = curr_Node.next

    def reverve(self):
        curr_Node = self.head
        previous = None
        while curr_Node != None:
            next = curr_Node.get_next()
            curr_Node.set_next(previous)
            prev = curr_Node
            curr_Node = next
        self.head = previous

    def clear(self):
        self.__init__()


my_list = Linked_List([1, 2, 3, 4])

# elements_to_add = [4, 2, 7, 9]
# my_list.create_list(elements_to_add)

my_list.append(4)
print(my_list.push_front(None))
print(my_list)
# my_list.remove_first()

my_list.show_List()
# my_list.list_lenght()
print(my_list.list_lenght())
print(my_list.searching_Element(2))
