from abc import ABC, abstractmethod


class Observer(ABC):
	@abstractmethod
	def update(self, state):
		pass


class Subject:

	def __init__(self):
		self.observers = set()

	def attach(self, observer):
		self.observers.add(observer)

	def detach(self, observer):
		self.observers.remove(observer)

	def notify(self):
		for observer in self.observers:
			observer.update(self._price)


class Stock(Subject):
	def __init__(self, name, price):
		super().__init__()
		self._name = name
		self._price = price

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		self._price = value
		self.notify()


class Investor(Observer):
	def __init__(self, name):
		self._name = name

	def update(self, price):
		print(f"Investor {self._name}: Stock price updated to {price}")


if __name__ == '__main__':
	# Create the ConcreteSubject
	stock = Stock("AAPL", 150)

	# Create ConcreteObservers
	investor1 = Investor("Alice")
	investor2 = Investor("Bob")

	# Attach observers to the subject
	stock.attach(investor1)
	stock.attach(investor2)

	# Change the stock price
	stock.price = 155  # Output: Investor Alice: Stock price updated to 155
	#         Investor Bob: Stock price updated to 155

	# Change the stock price again
	stock.price = 160  # Output: Investor Alice: Stock price updated to 160
	#         Investor Bob: Stock price updated to 160

	# Detach an observer and change the stock price
	stock.detach(investor1)
	stock.price = 165  # Output: Investor Bob: Stock price updated to 165