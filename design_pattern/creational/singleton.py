class SingletonMeta(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
	def __init__(self):
		self.value = None

	def set_value(self, value):
		self.value = value

	def get_value(self, value):
		self.value = value


if __name__ == '__main__':

	s1 = Singleton()
	s2 = Singleton()
	s3 = Singleton()
	s4 = Singleton()

	s1.set_value(22)
	s4.set_value(33)

	print(s1.value)
	print(s2.value)
	print(s3.value)
	print(s4.value)
	if id(s1) == id(s2):
		print("Singlgton workds")
	else:
		print("Singletion failed")