from abc import ABC, abstractmethod


class General(ABC):

	@abstractmethod
	def say(self):
		pass


class Colonel(General):
	def say(self):
		print("Yes sir, Im a Colonel")


class Captain(General):
	def say(self):
		print('Yes sir, Im a Captain')


class CompositeArmy(General):
	def __init__(self):
		self._armies = []

	def add(self, general):
		self._armies.append(general)

	def remove(self, general):
		self._armies.remove(general)

	def say(self):
		for it in self._armies:
			it.say()



if __name__ == '__main__':
	colonel = Colonel()

	captain1 = Captain()
	captain2 = Captain()

	composite = CompositeArmy()
	composite.add(colonel)
	composite.add(captain1)

	composite2 = CompositeArmy()
	composite2.add(composite)
	composite2.add(captain2)


	composite2.say()

