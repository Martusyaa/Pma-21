from node import Node
from linked_list import Linked_List


node_one = Node("A")
node_two = Node("B")
node_three = Node("C")

linList = Linked_List(node_one)
linList.add(node_two)
linList.add(node_three)

print(linList)