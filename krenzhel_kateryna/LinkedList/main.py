from List import LinkedList

dll = LinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
print(dll.display())

dll.prepend(0)
dll.insert(5, 5)
print(dll.display())

dll.delete(2)
print(dll.display())

list = LinkedList([1, 2, 3, 4, 5])
print(list.display())

list.insert(7, 3)
print(list.display())

list.append(9)
print(list.display())

list.clear()
print(list.display())


