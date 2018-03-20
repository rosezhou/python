def judge():
	year  = int(input("请输入年份:\t"))
	month = int(input("请输入月份\t"))
	day   = int(input("请输入几号\t"))
	name_Month(year,month,day)

def name_Month(year,month,myDay):
	day = 0
	big_Month   = [1,3,5,7,8,10,12]
	small_Month = [4,6,9,11]
	
	for i in range(1,month):
		if i in big_Month:
			day+=31	
		elif i in small_Month:
			day+=30

		else:
			if is_Leap(year):
				day+=29
			else:
				day+=28


	day+=myDay
	print("是%d的第%d天"%(year,day))






def is_Leap(year):
	if year%400 ==0 or (year%4 ==0 and year%100 !=0):
		return  1
	else:
		return  0


judge()
