from __future__ import annotations
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
	@abstractmethod
	def createChair(self) -> Chair:
		pass

	@abstractmethod
	def createSofa(self) -> Sofa:
		pass

	@abstractmethod
	def createCoffeeTable(self) -> CoffeeTable:
		pass


class ArtDecoFurnitureFactory(FurnitureFactory):
	def createChair(self) -> Chair:
		return ArtDecoChair()

	def createSofa(self) -> Sofa:
		return ArtDecoSofa()

	def createCoffeeTable(self) -> CoffeeTable:
		return ArtDecoCoffeeTable()


class VictorianFurnitureFactory(FurnitureFactory):
	def createChair(self) -> Chair:
		return VictorianChair()

	def createSofa(self) -> Sofa:
		return VictorianSofa()

	def createCoffeeTable(self) -> CoffeeTable:
		return VictorianCoffeeTable()


class ModernFurnitureFactory(FurnitureFactory):
	def createChair(self) -> Chair:
		return ModernChair()

	def createSofa(self) -> Sofa:
		return ModernSofa()

	def createCoffeeTable(self) -> CoffeeTable:
		return ModernCoffeeTable()


class Chair(ABC):
	@abstractmethod
	def hasLegs(self) -> str:
		pass

	@abstractmethod
	def sitOn(self) -> str:
		pass


class ArtDecoChair(Chair):
	def hasLegs(self) -> str:
		return "ArtDecoChair 4 legs"

	def sitOn(self) -> str:
		return "ArtDecoChair sit on living room"


class VictorianChair(Chair):
	def hasLegs(self) -> str:
		return "VictorianChair 4 legs"

	def sitOn(self) -> str:
		return "VictorianChair sit on living room"


class ModernChair(Chair):
	def hasLegs(self) -> str:
		return "ModernChair 4 legs"

	def sitOn(self) -> str:
		return "ModernChair sit on living room"


class Sofa(ABC):
	@abstractmethod
	def hasLegs(self) -> str:
		pass

	@abstractmethod
	def sitOn(self) -> str:
		pass


class ArtDecoSofa(Sofa):
	def hasLegs(self) -> str:
		return "ArtDecoSofa 4 legs"

	def sitOn(self) -> str:
		return "ArtDecoSofa sit on living room"


class VictorianSofa(Sofa):
	def hasLegs(self) -> str:
		return "VictorianSofa 6 legs"

	def sitOn(self) -> str:
		return "VictorianSofa sit on living room"


class ModernSofa(Sofa):
	def hasLegs(self) -> str:
		return "ModernSofa 6 legs"

	def sitOn(self) -> str:
		return "ModernSofa sit on bedroom"


class CoffeeTable(ABC):
	@abstractmethod
	def hasLegs(self) -> str:
		pass

	@abstractmethod
	def sitOn(self) -> str:
		pass


class ArtDecoCoffeeTable(CoffeeTable):
	def hasLegs(self) -> str:
		return "ArtDecoCoffeeTable 4 legs"

	def sitOn(self) -> str:
		return "ArtDecoCoffeeTable sit on living room"


class VictorianCoffeeTable(CoffeeTable):
	def hasLegs(self) -> str:
		return "VictorianCoffeeTable 6 legs"

	def sitOn(self) -> str:
		return "VictorianCoffeeTable sit on living room"


class ModernCoffeeTable(CoffeeTable):
	def hasLegs(self) -> str:
		return "ModernCoffeeTable 5 legs"

	def sitOn(self) -> str:
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
			raise Exception("You provided a type that is not supported")

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
