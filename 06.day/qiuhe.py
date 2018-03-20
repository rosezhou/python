def money(day):
	sum = day *30 #一个月三十天
	return sum
day = int(input("请输入一天赚多少钱 "))
print("一个月赚 %d"%money(day))
