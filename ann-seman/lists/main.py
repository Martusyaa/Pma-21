class ArrayList:
    def __init__(self):
        self.array = []

    def add(self, element):
        self.array.append(element)

    def remove(self, element):
        try:
            self.array.remove(element)
        except ValueError:
            raise ValueError("Елемент не знайдено у списку")

    def insert(self, index, element):
        if index < 0 or index > len(self.array):
            raise IndexError("Недійсний індекс")
        self.array.insert(index, element)

    def clear(self):
        self.array = []

    def display(self):
        print(self.array)


# Клас для реалізації LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove(self, element):
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        raise ValueError("Елемент не знайдено у списку")

    def insert(self, index, element):
        if index < 0:
            raise IndexError("Недійсний індекс")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is None:
                    raise IndexError("Недійсний індекс")
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if new_node.next:
                new_node.next.prev = new_node
            current.next = new_node

    def clear(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    array_list = ArrayList()
    linked_list = LinkedList()

    while True:
        print("Виберіть операцію:")
        print("1. Додати елемент")
        print("2. Видалити елемент")
        print("3. Вставити елемент")
        print("4. Вивести список")
        print("5. Очистити список")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            element = input("Введіть елемент: ")
            array_list.add(element)
            linked_list.add(element)
        elif choice == "2":
            element = input("Введіть елемент для видалення: ")
            array_list.remove(element)
            linked_list.remove(element)
        elif choice == "3":
            element = input("Введіть елемент: ")
            index = int(input("Введіть індекс: "))
            array_list.insert(index, element)
            linked_list.insert(index, element)
        elif choice == "4":
            print("ArrayList:")
            array_list.display()
            print("LinkedList:")
            linked_list.display()
        elif choice == "5":
            array_list.clear()
            linked_list.clear()
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 6.")
