class Dog(object):

	def __init__(self,name):
		self.name = name

	def game(slef):
		print(self.name + "在玩耍!")


class Xiaotianquan(Dog):

	def game(self):
		print(self.name + "在天上玩耍!")


class Person(object):

	def __init__(self,name):
		self.name = name

	def Game_with_dog(self,dog):
		print("%s和%s在玩耍!"%(self.name,dog.name))


#kuku = Dog("kuku")
feitianwangcai = Xiaotianquan("飞天旺财")
xiaoming = Person("小明")
xiaoming.Game_with_dog(feitianwangcai)