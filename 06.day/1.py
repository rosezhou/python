
def my_Message():
	name = "godzhou"
	age  = 21
	print("姓名:%s 年龄%d"%(name,age))


my_Message()




def show_sum(x,y,z):
	sum = x + y - z
	print("和:%d+%d-%d=%d"%(x,y,z,sum))


show_sum(4,5,7)



for i in range(1,10):
	for z in range(1,i+1):
		print("%d*%d=%d"%(z,i,z*i),end="\t")
	print("")




for i in range(100,201):
	number = True
	for z in range(2,i):
		if i % z == 0:
			number = False
			break
	if number == True:
		print(i)



year = int(input("请输入年份"))
def show_year(year):
	if (year % 400 == 0) or (year %  4 ==0) and (year % 100 !=0):
		print("你输入的%d是闰年"%year)
	else:
		print("你输入的%d是平年"%year)
show_year(year)

number = int(input("请输入一个和数: "))
number1 = int(input("请输入另一个和数: ")) 
def show_sum(number,number1):
	sum = number + number1
	print("%d+%d=%d"%(number,number1,sum))
show_sum(number,number1)

