class toast:
	def __init__(self):
		self.cookTime = 0
		self.cookStr  = "生得"
		self.list     = []
	def cook(self,time):
		self.cookTime += time
		if self.cookTime > 8:
			self.cookStr = "烤成炭了"
		elif self.cookTime > 5:
			self.cookStr = "烤熟了"
		elif self.cookTime > 3:
			self.cookStr = "半生不熟"
		else:
			self.cookStr = "生得"
	def __str__(self):
		msg = ""
		msg = self.cookStr + "地瓜"
		if len(self.list) > 0:
			for i in self.list:
				msg = msg + i + ","
			msg = msg.strip(",")
		return msg
	def addDosing(self,dosing):
		self.list.append(dosing)

mytoast = toast()
mytoast.cook(3)
print(mytoast.cookTime)
print(mytoast.cookStr)
print(mytoast.list)
mytoast.cook(3)
print(mytoast)
print("---添加番茄酱---")
mytoast.addDosing("番茄酱")
print(mytoast)
