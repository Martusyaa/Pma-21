from node import Node


class Linked_List:
    
    
    def __init__(self, head:Node):
        self.head = None
        
        
    def add(self, new_node:Node):
        node_iterator = self.head
        if self.head == None:
            self.head = new_node
        while node_iterator.next_node != None:
            if node_iterator.next_node == None:
                node_iterator.next_node = new_node
                break
            else:
                node_iterator = node_iterator.next_node
                
                
    def get_size(self):
        node_iterator = self.head
        size_value_to_return = 1
        while node_iterator.next_node != None:
            size_value_to_return += 1
        return size_value_to_return
            
                
                
    def add_index(self, node:Node, index):
        node_iterator = self.head
        if index == 0:
            self.head = node
        elif self.get_size() < index - 1:
            raise IndexError
        elif index < 0:
            raise IndexError
        else:
            for i in index:
                node_iterator = node_iterator.next_node
            node_iterator.next_node = node
                
    
    def __str__(self):
        node_iterator = self.head
        while node_iterator.next_node != None:
            print(node_iterator)
        print(node_iterator.next_node)