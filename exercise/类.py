class Restaurant(object):
	def __init__(self,name,type):
		self.restaurant_name = name
		self.cuisine_type = type
		self.count = 0
	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)

	def open_restaurant(self):
		print("正在营业")

	def number_served(self):
		
		print("一共就餐" + str(self.count) + "个人!")

	def set_number_served(self,number):
		restaurant.count = number
		print("一共就餐" + str(self.count) + "个人!")

	def increment_number_served(self,num):
		restaurant.count += num
		print("一共就餐" + str(self.count) + "个人!") 
"""
restaurant = Restaurant("小周烤翅","烤翅")

restaurant.increment_number_served(100)
restaurant.set_number_served(50)
restaurant.number_served()
restaurant.count = 23
restaurant.number_served()

restaurant = Restaurant("小周烤翅","烤翅")
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""

class IceCreamStand(Restaurant):

	def bing_qi_lin(self):
		flavors = ["草莓味","樱桃味","榴莲味","韭菜味"]
		for i in flavors:
			print("冰淇淋都有:" + i)

bingqilin = IceCreamStand("冰雪天地","冰淇淋")
bingqilin.describe_restaurant() 
bingqilin.open_restaurant()
bingqilin.bing_qi_lin()
















