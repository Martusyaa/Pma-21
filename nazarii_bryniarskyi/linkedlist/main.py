from LinkedList import LinkedList


def main():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)

    linked_list2 = LinkedList(linked_list)
    linked_list2.remove(0)

    print(linked_list.get(0))


main()
