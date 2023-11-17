from ClassList import LinkedList
if __name__ == '__main__':
    list_elements = [1,2,3]
    linked_list = LinkedList(elements=list_elements)

    linked_list.add_to_end(4)
    linked_list.add_to_end(5)
    linked_list.add_to_end(6)
    linked_list.add_to_start(0)
    print("Елементи списку:", linked_list.show())

try:
    linked_list.insert(4, 3)
    print("Список після додавання елементу за індексом:", linked_list.show())
except IndexError as e:
    print(e)

try:
    linked_list.delete(2)
    print("Після видалення:", linked_list.show())
except ValueError as e:
    print(e)

try:
    linked_list.clear()
    print("Після очищення:", linked_list.show())
except ValueError as e:
    print(e)