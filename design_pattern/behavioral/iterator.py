from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable


class ConcrteIterator(Iterator):
	def __init__(self, coolection):
		self._collection = coolection
		self._index = 0

	def __next__(self):
		try:
			value = self._collection[self._index]
		except IndexError:
			raise StopIteration()
		self._index += 1
		return value

	def has_next(self):
		return self._index < len(self._collection)


class ConcreteAggregate(Iterable):
	def __init__(self):
		self._items = []

	def __iter__(self):
		return ConcrteIterator(self._items)

	def add_item(self, item):
		self._items.append(item)


if __name__ == '__main__':
	aggregate = ConcreteAggregate()
	aggregate.add_item('Item 1')
	aggregate.add_item('Item 2')
	aggregate.add_item('Item 3')

	# Explicit usage of ConcreteIterator
	iterator = iter(aggregate)
	while iterator.has_next():
		print(next(iterator))

	# print("-----")
	#
	# # Implicit usage of ConcreteIterator (Pythonic way)
	# for item in aggregate:
	# 	print(item)
