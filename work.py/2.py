#猜数字
import random

computer = random.randint(1,100)
count = 0
while count < 10:
	me = int(input("请输入数字1 - 100:\t"))
	if me > computer:
		print("你输入的数字大了")
	elif me < computer:
		print("你输入的数字小了")
		count+=1
	else:
		print("你猜对了")
		break
			 
