
class Queue:

	def __init__(self):
		self.queue = []
		self.length = 0

	def dequeue(self):
		if self.queue:
			self.length -= 1
			return self.queue.pop(0)
		return None

	def enqueue(self, item):
		try:
			self.queue.append(item)
			self.length += 1
			return True
		except:
			return False

	def peek(self):
		if self.queue:
			return self.queue[0]
		return None

	def is_empty(self):
		return True if self.queue else False

	def size(self):
		return self.length
