class House:

	def __init__(self):
		self.floors = 0
		self.windows = 0
		self.doors = 0
		self.rooms = 0
		self.hasGarage = False
		self.hasSwimPool = False
		self.hasStatues = False
		self.hasGarden = False

	def __str__(self):
		return """My house has: {} floors, {} windows, {} doors, {} rooms, Garage: {}, Swimming Pool: {},
			Statues: {}, Garden: {}""".format(
			self.floors, self.windows, self.doors, self.rooms,
			self.hasGarage, self.hasSwimPool, self.hasStatues, self.hasGarden
		)


class HouseBuilder:
	def __init__(self):
		self.house = House()

	def build_floors(self, n):
		self.house.floors = n
		return self

	def build_windows(self, n):
		self.house.windows = n
		return self

	def build(self):
		return self.house


class Director:

	def __init__(self, builder):
		self.builder = builder

	def contruct_big_house(self):
		self.builder.build_windows(6).build_floors(2)
		return self.builder.build()


if __name__ == '__main__':
	builder = HouseBuilder()
	director = Director(builder)
	my_house = director.contruct_big_house()
	print(my_house)
