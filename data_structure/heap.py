class MaxHeap:

	def __init__(self):
		self.heap = []

	def get_left_child(self, idx):
		return (2 * idx) + 1

	def get_right_child(self, idx):
		return (2 * idx) + 2

	def get_parent(self, idx):
		return (idx - 1) // 2

	def insert(self, value):
		idx = len(self.heap)
		self.heap.append(value)
		print("xxxx", self.heap[idx])
		while self.heap[self.get_parent(idx)] < self.heap[idx] and idx > 0:
			self.heap[self.get_parent(idx)], self.heap[idx] = self.heap[idx], self.heap[self.get_parent(idx)]
			idx = self.get_parent(idx)

	def extract_max(self):
		idx = 0
		res = self.heap[idx]
		self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
		self.heap.pop()
		print(self.heap)
		while self.heap[idx] < self.heap[self.get_left_child(idx)] or self.heap < self.heap[self.get_right_child(idx)]:
			l = self.get_left_child(idx)
			r = self.get_right_child(idx)
			if self.heap[l] > self.heap[r]:
				self.heap[idx], self.heap[l] = self.heap[l], self.heap[idx]
				idx = l
			else:
				self.heap[idx], self.heap[r] = self.heap[r], self.heap[idx]
				idx = r
			if self.get_left_child(idx) >= len(self.heap):
				break

		return res

	def heapify(self):
		...


if __name__ == '__main__':
	heap = MaxHeap()
	heap.heap = [55, 22, 33, 11, 15, 25, 27]

	heap.insert(77)

	print(heap.extract_max())
	print(heap.heap)