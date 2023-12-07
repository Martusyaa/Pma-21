class Node:


	def __init__(self, value, next_node=None, previous_node=None):
		self.value = value
		self.next = next_node
		self.previous = previous_node
  
	def __str__(self):
		return f"{self.value}"
