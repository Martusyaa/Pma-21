class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, elements=[]):
        self.entrance = None
        self.exit = None
        for element in elements:
            self.make_magic_happen(element)

    def make_magic_happen(self, data):
        magic_node = Node(data)
        if not self.entrance:
            self.entrance = magic_node
            self.exit = magic_node
        else:
            magic_node.prev = self.exit
            self.exit.next = magic_node
            self.exit = magic_node

    def perform_ritual_at_start(self, data):
        magical_node = Node(data)
        if not self.entrance:
            self.entrance = magical_node
            self.exit = magical_node
        else:
            magical_node.next = self.entrance
            self.entrance.prev = magical_node
            self.entrance = magical_node

    def cast_spell_at_index(self, data, index):
        magical_node = Node(data)
        current_spell = self.entrance
        magic_count = 0
        try:
            while current_spell:
                if magic_count == index:
                    magical_node.next = current_spell
                    magical_node.prev = current_spell.prev
                    if current_spell.prev:
                        current_spell.prev.next = magical_node
                    else:
                        self.entrance = magical_node
                    current_spell.prev = magical_node
                    return
                magic_count += 1
                current_spell = current_spell.next

            if magic_count == index:
                self.exit.next = magical_node
                magical_node.prev = self.exit
                self.exit = magical_node
                return
            if magic_count < index:
                raise IndexError(ERROR)
        except IndexError as e:
            print("Magic Error: ", e)

    def dispel_magic_at_data(self, data):
        current_spell = self.entrance
        while current_spell:
            if current_spell.data == data:
                if current_spell.prev:
                    current_spell.prev.next = current_spell.next
                else:
                    self.entrance = current_spell.next
                if current_spell.next:
                    current_spell.next.prev = current_spell.prev
                else:
                    self.exit = current_spell.prev
                return
            current_spell = current_spell.next

    def banish_all_magic(self):
        self.entrance = None
        self.exit = None

    def reveal_mysteries(self):
        magic_elements = []
        current_spell = self.entrance
        while current_spell:
            magic_elements.append(current_spell.data)
            current_spell = current_spell.next
        return magic_elements

    def display(self):
        return self.reveal_mysteries()

# Приклад використання
magic_list = LinkedList([1, 2, 3, 4])
print("Original List:", magic_list.display())

magic_list.perform_ritual_at_start(0)
print("List after performing ritual at start:", magic_list.display())

magic_list.cast_spell_at_index(5, 2)
print("List after casting spell at index 2:", magic_list.display())

magic_list.dispel_magic_at_data(3)
print("List after dispelling magic at data 3:", magic_list.display())

magic_list.banish_all_magic()
print("List after banishing all magic:", magic_list.display())