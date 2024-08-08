from abc import ABC, abstractmethod


class Strategy(ABC):
	@abstractmethod
	def do_algorithm(self, data):
		pass


class SortStategy(Strategy):
	def do_algorithm(self, data):
		return sorted(data)


class ReverseStrategy(Strategy):
	def do_algorithm(self, data):
		return data[::-1]


class Context:

	def __init__(self, strategy: Strategy):
		self._strategy = strategy

	@property
	def strategy(self):
		return self._strategy

	@strategy.setter
	def strategy(self, strategy):
		self._strategy = strategy

	def execute_algorithm(self, data):
		print('Execute algorithm')
		print(self._strategy.do_algorithm(data))


if __name__ == '__main__':
	sort_strategy = SortStategy()
	reverse_strategy = ReverseStrategy()

	data = [5, 7, 1, 6, 3, 4]
	context = Context(sort_strategy)

	context.execute_algorithm(data)
	context.strategy = reverse_strategy
	context.execute_algorithm(data)
