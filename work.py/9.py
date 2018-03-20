path = float(input("请输入家到学校的路程：\t"))
money = 0
sum = 0
#小明一天坐2趟,假如一个月都是30天
for i in range(1,61):
	if path <= 6:
		money = 3#6公里(含)内3块
	elif path > 6 and path <= 12:
		money = 4#6公里至12公里(含)4块
	elif path > 12 and path <=22:
		money = 5#12公里至22公里(含)5块
	elif path > 22 and path <= 32:
		money = 6#22公里至32公里(含)6块
	elif path > 32:
		if (path-32)%20 == 0:
			money = 6+(path-32)/20
		else:
			money = 6+(int(path-32)/20)+1
	if sum >= 100 and sum < 150:
		money = money*0.8
	elif sum >= 150 and sum <400:
		money = money*0.5
	sum+=money
print("坐地铁一个月花%.2f"%sum)

