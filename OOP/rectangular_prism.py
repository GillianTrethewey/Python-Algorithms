class RectangularPrism:

	def __init__(self, height, width, depth):
		self.height = height
		self.width = width
		self.depth = depth

	def get_val(self):
		print("The height of: ", self, " is ", self.height)

	def get_volume(self):
		v = self.height * self.width * self.depth
		print("The volume is: ", v) 


prism_1 = RectangularPrism(10, 20, 5)
prism_2 = RectangularPrism(15, 10, 10)
prism_1.get_val()
prism_1.get_volume()
