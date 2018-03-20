class Aniaml(object):
	#init 魔法方法
	def __init__(self):
		self.pin_zhong = "动物"

	#方法行为   输出品种
	def print_name(self):
		print("鲜花插在牛粪上")
"""
dog = Animal()
dog.breed = "hapagou"
dog.print_name()
"""

class Dog(Aniaml):
	def pao(self):
		print("狗在跑")

	def print_name(self):
		super().print_name()
		print("烂蛤蟆")

	def cry(self):
		print("狗在哭")

"""
kuku = Dog()
kuku.pin_zhong = "狗"
kuku.print_name()
kuku.pao()
"""

class Cat(Aniaml):
	def miao(self):
		print("貓在叫")

	def cry(self):
		print("貓在哭")

class Luangao(Dog,Cat):
	pass

d = Dog()
d.print_name()



"""
a = Luangao()
a.cry()
"""

"""
a = Luangao()
a.pao()
a.miao()
a.pin_zhong = "貓狗兽"
a.print_name()
"""
