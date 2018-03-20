import random
class Zhourunlin_Caishuzi(object):
	def __init__(self):
		self.zhou = 1
		self.run = 1

		self.dic = {}



	def zhourunlin_number(self):

		zhourunlin_num = random.randint(0,99)
		print("猜数字游戏开始了")

		while True:
			zhourunlin = int(input("请输入一个数字:"))
			self.zhou += 1
			#判断数字
			if zhourunlin > zhourunlin_num:

				print("你输入的数字大了")
				
		
			elif zhourunlin < zhourunlin_num:

				print("你输入的数字小了")
				
	
			else:
				print("你猜对了")
				#是否继续玩
				zhourunlin_me = int(input("1 继续 2 结束: "))
				if zhourunlin_me == 1:
					self.run += 1
					z = self.zhou
					x = self.run
					self.dic[x] = z
					self.zhourunlin_number()
				
				if zhourunlin_me == 2:
					
					print("你一共玩了:" + str(self.run) + "局")
					for k,v in self.dic.items():
						print("第%d次游戏猜了%d次"%(k,v))

					break


number1 = Zhourunlin_Caishuzi()
number1.zhourunlin_number()
