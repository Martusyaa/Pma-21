class Linked_list:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        to_return = []
        node_iterator = self.head
        while node_iterator is not None:
            to_return.append(node_iterator.value)
            node_iterator = node_iterator.next
        return str(to_return)
        
    def appendleft(self, new_head):
        old_head = self.head
        self.head = new_head
        self.head.next = old_head
        
    def append(self, new_node):
        node_iterator = self.head
        if self.head == None:
            self.head = new_node
        while node_iterator != None:
            if(node_iterator.next is None):
                node_iterator.next = new_node
                break
            else:
                node_iterator = node_iterator.next
                
    
    def remove_by_val(self, value):
        node_iterator = self.head
        if node_iterator.value == value:
            self.head = node_iterator.next
            node_iterator = None
            return
        while node_iterator != None:
            if node_iterator.value == value:
                node_iterator.value = node_iterator.next.value
                node_iterator.next = node_iterator.next.next
                break
            node_iterator = node_iterator.next