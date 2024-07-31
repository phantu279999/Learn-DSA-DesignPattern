from __future__ import annotations
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
	@abstractmethod
	def createChair(self):
		return Chair()

	@abstractmethod
	def createSofa(self):
		return Sofa()

	@abstractmethod
	def createCoffeeTable(self):
		return CoffeeTable()


class ArtDecoFurnitureFactory(FurnitureFactory):
	def createChair(self):
		return ArtDecoChair()

	def createSofa(self):
		return ArtDecoSofa()

	def createCoffeeTable(self):
		return ArtDecoCoffeeTable()


class VictorianFurnitureFactory(FurnitureFactory):
	def createChair(self):
		return VictorianChair()

	def createSofa(self):
		return VictorianSofa()

	def createCoffeeTable(self):
		return VictorianCoffeeTable()


class ModernFurnitureFactory(FurnitureFactory):
	def createChair(self):
		return ModernChair()

	def createSofa(self):
		return ModernSofa()

	def createCoffeeTable(self):
		return ModernCoffeeTable()


class Chair(ABC):
	@abstractmethod
	def hasLegs(self):
		return "Chair 4 legs"

	@abstractmethod
	def sitOn(self):
		return "Chair sit on living room"


class ArtDecoChair(Chair):
	def hasLegs(self):
		return "ArtDecoChair 4 legs"

	def sitOn(self):
		return "ArtDecoChair sit on living room"


class VictorianChair(Chair):
	def hasLegs(self):
		return "VictorianChair 4 legs"

	def sitOn(self):
		return "VictorianChair sit on living room"


class ModernChair(Chair):
	def hasLegs(self):
		return "ModernChair 4 legs"

	def sitOn(self):
		return "ModernChair sit on living room"


class Sofa(ABC):
	@abstractmethod
	def hasLegs(self):
		return "Sofa 4 legs"

	@abstractmethod
	def sitOn(self):
		return "Sofa sit on living room"


class ArtDecoSofa(Chair):
	def hasLegs(self):
		return "ArtDecoSofa 4 legs"

	def sitOn(self):
		return "ArtDecoSofa sit on living room"


class VictorianSofa(Chair):
	def hasLegs(self):
		return "VictorianSofa 6 legs"

	def sitOn(self):
		return "VictorianSofa sit on living room"


class ModernSofa(Chair):
	def hasLegs(self):
		return "ModernSofa 6 legs"

	def sitOn(self):
		return "ModernSofa sit on bedroom"


class CoffeeTable(ABC):
	@abstractmethod
	def hasLegs(self):
		return "CoffeeTable 4 legs"

	@abstractmethod
	def sitOn(self):
		return "CoffeeTable sit on living room"


class ArtDecoCoffeeTable(Chair):
	def hasLegs(self):
		return "ArtDecoCoffeeTable 4 legs"

	def sitOn(self):
		return "ArtDecoCoffeeTable sit on living room"


class VictorianCoffeeTable(Chair):
	def hasLegs(self):
		return "VictorianCoffeeTable 6 legs"

	def sitOn(self):
		return "VictorianCoffeeTable sit on living room"


class ModernCoffeeTable(Chair):
	def hasLegs(self):
		return "ModernCoffeeTable 5 legs"

	def sitOn(self):
		return "ModernCoffeeTable sit on living room"


class Client:

	def __init__(self, config):
		if config['type'] == 'ArtDeco':
			self.factory = ArtDecoFurnitureFactory()
		elif config['type'] == 'Victorian':
			self.factory = VictorianFurnitureFactory()
		elif config['type'] == 'Modern':
			self.factory = ModernFurnitureFactory()
		else:
			raise Exception("You provide type current hasn't")

	def main(self) -> None:
		product_a = self.factory.createChair()
		product_b = self.factory.createSofa()
		product_c = self.factory.createCoffeeTable()
		print(f"{product_a.hasLegs()}")
		print(f"{product_a.sitOn()}")
		print(f"{product_b.hasLegs()}")
		print(f"{product_b.sitOn()}")
		print(f"{product_c.hasLegs()}")
		print(f"{product_c.sitOn()}")


if __name__ == '__main__':
	config = {
		'type': 'Modern'
	}
	client = Client(config)
	client.main()

