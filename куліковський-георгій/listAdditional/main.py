from node import Node
from linked_list import Linked_list


node_one = Node("First node")
node_two = Node("Second node")
node_three = Node("Third node")
node_one.next = node_two
node_two.next = node_three

list_one = Linked_list()
list_one.head = node_one
list_one.appendleft(Node("Left node"))
list_one.append(Node("Fourth node"))
list_one.remove_by_val("Second node")
print(list_one)