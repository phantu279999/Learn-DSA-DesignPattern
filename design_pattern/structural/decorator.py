from abc import ABC, abstractmethod


class Component(ABC):

	@abstractmethod
	def excute(self):
		pass


class ConcreteComponent(Component):

	def excute(self):
		print("Component 1")


class ConcreteComponent2(Component):

	def excute(self):
		print("Component 2")


class Decorator(Component):
	_component: Component = None

	def __init__(self, component: Component):
		self._component = component

	@property
	def component(self) -> Component:
		return self._component

	def excute(self) -> str:
		return self._component.excute()


class DecoratorA(Decorator):

	def excute(self) -> str:
		return "Decorator A: {}".format(self.component.excute())


class DecoratorB(Decorator):

	def excute(self) -> str:
		return "Decorator A: {}".format(self.component.excute())


def client_code(component: Component) -> None:
	print(f"RESULT: {component.excute()}")


if __name__ == "__main__":
	simple = ConcreteComponent()
	print("Client: I've got a simple component:")
	client_code(simple)
	print("\n")

	decorator1 = DecoratorA(simple)
	decorator2 = DecoratorB(decorator1)
	print("Client: Now I've got a decorated component:")
	client_code(decorator2)


