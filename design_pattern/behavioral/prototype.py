import copy
from PIL import Image


class ImagePrototype:

	def __init__(self, image_path):
		self.image = Image.open(image_path)

	def clone(self):
		return copy.deepcopy(self)

	def resize(self, width, height):
		self.image = self.image.resize((width, height))

	def crop(self, box):
		self.image = self.image.crop(box)

	def filter(self, filter):
		self.image = self.image.filter(filter)


class JPGImage(ImagePrototype):
	def __init__(self, image_path):
		super().__init__(image_path)


if __name__ == "__main__":
	my_image = JPGImage(r'G:\Py\DSAWP\image-home-22.jpg')

	clone = my_image.clone()
	clone.resize(200, 200)

	print(my_image.image.size)
	print(clone.image.size)
	# (445, 535)
	# (200, 200)
