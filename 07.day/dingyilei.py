class Car():
	def __init__(self,newname,price):

		self.name = newname
		self.price = price
	def print_price(self):
		print("%s,%s"%(self.name,self.price))

BMW = Car("宝马","五十万")
BMW.print_price()

BC = Car("奔驰","四十五万")
BC.print_price()

AD = Car("奥迪","四十万")
AD.print_price()
