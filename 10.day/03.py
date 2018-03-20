class Car(object):
	#Count = 0

	#类方法
	@classmethod
	def move(cls):
		print("车在移动")

	@staticmethod
	def benpao():
		print("车在跑")

	def __init__(self):
		self.color = "red"

Car.benpao()

a = Car()
a.benpao()

b = Car()
b.benpao()
#print(Car.Count)
#Car.move()


