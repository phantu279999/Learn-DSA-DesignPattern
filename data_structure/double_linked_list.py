class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None


class DoubleLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		temporary = self.head
		while temporary.next:
			temporary = temporary.next
		temporary.next = new_node
		new_node.prev = temporary
		self.tail = new_node

	def insert(self, data, position):
		...

	def remove(self, data):
		...

	def display_left_to_right(self):
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next
		print()

	def display_right_to_left(self):
		temp = self.tail
		while temp:
			print(temp.data, end=' ')
			temp = temp.prev
		print()


if __name__ == '__main__':
	ll = DoubleLinkedList()
	ll.append(1)
	ll.append(2)
	ll.append(3)
	ll.append(4)
	ll.append(6)
	ll.append(7)
	ll.display_right_to_left()
	ll.display_left_to_right()