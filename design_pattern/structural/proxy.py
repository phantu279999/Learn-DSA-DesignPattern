from abc import ABC, abstractmethod


class Object(ABC):

	@abstractmethod
	def request(self):
		pass


class SubObject(Object):

	def request(self):
		print("SubObject is here")


class Proxy:

	def __init__(self, obj: Object):
		self.obj = obj

	def request(self):
		print("Check:")
		print("Access Control")
		print("Lazy initialization")
		print("Logging")
		self.obj.request()


def client_code(proxy):

	proxy.request()


if __name__ == '__main__':
	obj = SubObject()
	proxy = Proxy(obj)

	client_code(proxy)
