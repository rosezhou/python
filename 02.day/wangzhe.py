#在腾讯储存的帐号
myZhanghao = 1219012957
myPasswd  = 321123


#个人登录操作
z =  0 
while z <= 3:
	
	account = int(input("请输入帐号:\n"))
	passwd  = int(input("请输入密码:\n"))

	if account == myZhanghao and passwd == myPasswd:
		print("登录成功")
		hero = int(input("请选择英雄范围:0 adc 1 肉 2 法师"))
		if hero == 0:
			print("鲁班大师")
		elif hero == 1:
			print("程咬金")
		elif hero == 2:
			print("王昭君")
			z = 5
	if account != myAccount and passwd != myPasswd:
		if z == 3:
			print("帐号被冻结了")
		else:
			print("登录失败，请重新输入:")
		z+=1




