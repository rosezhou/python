#预先设定的帐号密码
account = "123456"
passwd  = "321123"
#用户登录操作
for i in range(0,3):
	myAccount = input("请输入帐号")
	myPasswd  = input("请输入密码")
	if (myAccount) != account and (myPasswd != passwd):
		print("你的帐号或密码不正确，请重新输入")
	else:
		print("欢迎来到god周的世界")
		break
