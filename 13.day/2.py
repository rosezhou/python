class Houselftem(object):

	def __init__(self,name,free_area):

		#家具名称  占地面积
		self.name = name
		self.free_area = free_area

	def __str__(self):
		return "%s占地面积%.2f"%(self.name,self.free_area)
		

bed = Houselftem("席梦思", 4)
chest = Houselftem("衣柜", 2)
table = Houselftem("餐桌", 1.5)
print(bed)
print(chest)
print(table)





class House(Houselftem):

	def __init__(self,house_type,area):

		# 户型  总面积	
		self.house_type = house_type
		self.area = area
		self.list = []

	#添加家具
	def add_item(self):
		self.list.append(bed,chest,table)
		print(self.list)
	def __str__(self):
		return "户型:%s 总面积:%.2f 添加完家具剩余面积:%.2f"%(self.house_type,self.area,self.area-(4+2+1.5))

my_home = House("四室一厅一卫",200)
print(my_home)
my_home.add_item()	
