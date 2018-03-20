class Cat(object):
	def __init__(self,name):
		self.name = name
		self.color = "red"


class Bosi(Cat):
	def __init__(self,name):
		super().__init__(name)


	def getName(self):
		return self.name


bosi = Bosi("baihuzi")
print(bosi.name)
print(bosi.color)
