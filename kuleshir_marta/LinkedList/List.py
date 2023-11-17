class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if not cur_node:
            self.head = new_node
            return
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
        new_node.set_prev(cur_node)

    def delete(self, data):
        try:
            current = self.head
            while current:
                if current.get_data() == data:
                    prev_node = current.get_prev()
                    next_node = current.get_next()

                    if prev_node:
                        prev_node.set_next(next_node)
                    else:
                        self.head = next_node

                    if next_node:
                        next_node.set_prev(prev_node)

                    return True
                current = current.get_next()
            raise ValueError(f"Немає такого числа: {data}")
        except ValueError as e:
            print(f"Помилка: {e}")
            return False

    def insert_at_index(self, index, data):
        try:
            if index < 0:
                raise IndexError("Індекс повинен бути додатнім числом")
            new_node = Node(data)
            current = self.head
            for i in range(index):
                if current is None:
                    raise IndexError("Не існує такого індексу")
                current = current.get_next()
            prev_node = current.get_prev()

            if prev_node:
                prev_node.set_next(new_node)
                new_node.set_prev(prev_node)
            else:
                self.head = new_node
            new_node.set_next(current)
            current.set_prev(new_node)
        except IndexError as e:
            print(f"Помилка: {e}")

    def delete_at_index(self, index):
        try:
            if index < 0:
                raise IndexError("Індекс повинен бути додатнім числом")
            current = self.head
            for i in range(index):
                if current is None:
                    raise IndexError("Не існує такого індексу")
                current = current.get_next()

            prev_node = current.get_prev()
            next_node = current.get_next()

            if prev_node:
                prev_node.set_next(next_node)
            else:
                self.head = next_node

            if next_node:
                next_node.set_prev(prev_node)
        except IndexError as e:
            print(f"Помилка: {e}")

    def clear(self):
        current = self.head
        while current:
            next_node = current.get_next()
            current.set_prev(None)
            current.set_next(None)
            current = next_node
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Початковий зв'язаний список:")
linked_list.display()

linked_list.delete(1)

print("Зв'язаний список після видалення:")
linked_list.display()

linked_list.insert_at_index(7, 5)

print("Зв'язаний список після вставки:")
linked_list.display()

linked_list.delete_at_index(2)

print("Зв'язаний список після видалення:")
linked_list.display()

linked_list.clear()

print("Зв'язаний список після очищення:")
linked_list.display()
