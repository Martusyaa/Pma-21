from LinkedList import LinkedList

linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)


linked_list.pop(1)

for i in range(linked_list.size()):
    print(linked_list.print(i))

print()

linked_list.add(1,1)

for i in range(linked_list.size()):
    print(linked_list.print(i))

linked_list.clear()

for i in range(linked_list.size()):
    print(linked_list.print(i))
