from abc import ABC, abstractmethod


class Command(ABC):

	@abstractmethod
	def execute(self, data):
		pass


class CreateCommand(Command):

	def __init__(self, receiver):
		self.receiver = receiver

	def execute(self, data):
		self.receiver.create(data)

class UpdateCommand(Command):

	def __init__(self, receiver):
		self.receiver = receiver

	def execute(self, data):
		self.receiver.update(data)

class DeleteCommand(Command):

	def __init__(self, receiver):
		self.receiver = receiver

	def execute(self, data):
		self.receiver.delete(data)


class Receiver:

	def __init__(self):
		self.datas = set()

	def create(self, data):
		print("Create: {}".format(data))
		self.datas.add(data['data'])

	def update(self, data):
		print("Update: {}".format(data))
		self.datas.update(data['data'])

	def delete(self, data):
		print("Delete: {}".format(data))
		self.datas.remove(data['data'])


# Invoker
class Editor:
	def __init__(self):
		self.commands = {}

	def set_commands(self, action_type, command):
		self.commands[action_type] = command

	def execute(self, action):
		if action['type'] in self.commands:
			self.commands[action['type']].execute(action)


if __name__ == '__main__':
	receiver = Receiver()
	create = CreateCommand(receiver)
	update = UpdateCommand(receiver)
	delete = DeleteCommand(receiver)

	editor = Editor()
	editor.set_commands('create', create)
	editor.set_commands('update', update)
	editor.set_commands('delete', delete)

	actions = [
		{
			'type': 'create',
			"data": 'Book'
		},
		{
			'type': 'delete',
			"data": 'Book'
		},
	]
	for action in actions:
		editor.execute(action)
		print(receiver.datas)