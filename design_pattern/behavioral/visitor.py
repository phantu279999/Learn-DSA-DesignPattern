from abc import ABC, abstractmethod


# Visitor Interface
class ShapeVisitor(ABC):
	@abstractmethod
	def visit_circle(self, circle):
		pass

	@abstractmethod
	def visit_square(self, square):
		pass


class AreaCalculator(ShapeVisitor):
	def visit_circle(self, circle):
		area = 3.14 * (circle.radius ** 2)
		print("Circle area: {}".format(area))

	def visit_square(self, square):
		area = square.side * square.side
		print("Square are: {}".format(area))


# Concrete Visitor for Drawing
class DrawVisitor(ShapeVisitor):
	def visit_circle(self, circle):
		print(f"Drawing a circle with radius {circle.radius}")

	def visit_square(self, square):
		print(f"Drawing a square with side {square.side}")


# Element Interface
class Shape(ABC):
	@abstractmethod
	def accept(self, visitor: ShapeVisitor):
		pass


# Concrete Elements
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def accept(self, visitor: ShapeVisitor):
		visitor.visit_circle(self)


class Square(Shape):
	def __init__(self, side):
		self.side = side

	def accept(self, visitor: ShapeVisitor):
		visitor.visit_square(self)


if __name__ == '__main__':
	circle = Circle(5)
	square = Square(4)

	area_calculator = AreaCalculator()
	drawing_area = DrawVisitor()

	circle.accept(area_calculator)
	square.accept(area_calculator)

	square.accept(drawing_area)
	square.accept(drawing_area)
