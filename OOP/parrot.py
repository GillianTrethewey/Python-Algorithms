class Parrot:
	species = "bird"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getval(self):
		print(self.name)

obj = Parrot("Blue",20)
print(obj)
obj.getval()


