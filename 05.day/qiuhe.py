def sumnumber():
	sum = 0
	for i in range(1,101):
		sum = sum + i 
	print("总和：%d\t"%sum)

def even_number():
	sum = 0
	for j in range(1,101):
		if j%2 == 0:
			sum = sum + j
	print("偶数和:%d\t"%sum)

def odd_number():
	sum = 0
	for k in range(1,101):
		if k%2 !=0:
			sum = sum + k 
	print("奇数和:%d\t"%sum)
sumnumber()
even_number()
odd_number()
