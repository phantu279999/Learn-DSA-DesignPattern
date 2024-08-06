from abc import ABC, abstractmethod


class Handler(ABC):

	@abstractmethod
	def set_next(self, handler):
		pass

	@abstractmethod
	def handler(self, request):
		pass


class AbstractHandler(Handler):

	def __init__(self, handler=None):
		self._next_handler = handler

	def set_next(self, handler):
		self._next_handler = handler
		return handler

	def handler(self, request):
		if self._next_handler:
			self._next_handler.handler(request)
		return None


class ValidHandler(AbstractHandler):

	def handler(self, request):
		if request == 'Employee':
			return "Handler Valid is Processing"
		elif self._next_handler:
			return self._next_handler.handler(request)


class PermissionHandlerTwo(AbstractHandler):

	def handler(self, request):
		if request == 'Engineer':
			return "Handler Permission is Processing"
		elif self._next_handler:
			return self._next_handler.handler(request)


class LegalHandler(AbstractHandler):

	def handler(self, request):
		if request == 'Boss':
			return "Handler Legal is Processing"
		elif self._next_handler:
			return self._next_handler.handler(request)


def client_code(handler):

	for request in ['Boss', 'Engineer', 'Employee']:
		print(handler.handler(request))


if __name__ == '__main__':
	handler_1 = ValidHandler()
	handler_2 = PermissionHandlerTwo()
	handler_3 = LegalHandler()

	handler_1.set_next(handler_2)
	handler_2.set_next(handler_3)

	client_code(handler_1)
