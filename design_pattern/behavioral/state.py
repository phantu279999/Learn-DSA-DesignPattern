from abc import ABC, abstractmethod


class State(ABC):
	@abstractmethod
	def handle(self, context):
		pass


class TypingState(State):

	def handle(self, context):
		print("Typing: User is typing...")
		context.state = SavingState()


class SavingState(State):
	def handle(self, context):
		print("Saving: Document is being saved...")
		context.state = TypingState()


class ErrorState(State):
	def handle(self, context):
		print("Error: An error occurred!")
		context.state = TypingState()


class TextEditorContext:
	def __init__(self):
		self._state = TypingState()

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, state):
		self._state = state

	def request(self):
		self._state.handle(self)


if __name__ == '__main__':
	typing_state = TypingState()
	saving_state = SavingState()
	error_state = ErrorState()

	context = TextEditorContext()
	context.request()

	# Change state
	context.state = saving_state
	context.request()

	context.request()



"""
+---------------+
|    Context    |
+---------------+
| -state: State |
+---------------+
| +request()    |
| +setState()   |
+---------------+
        |
        v
+-----------------+
|      State      |
+-----------------+
| +handle(context: Context) |
+-----------------+
        ^
        |
        +----------------------+
        |                      |
+----------------+     +------------------+
| ConcreteStateA |     | ConcreteStateB   |
+----------------+     +------------------+
| +handle(c: Context)  | +handle(c: Context)  |
+----------------+     +------------------+

"""
