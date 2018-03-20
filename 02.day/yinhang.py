#这是银行云端的账户信息
account = 123456
passwd  = 321123
money   = 238

#这是个人操作的信息
myAccount = int(input("请输入帐号"))
myPasswd  = int(input("请输入密码"))
if myAccount == account and myPasswd == passwd:
	print("登录成功")
	mode = int(input("请选择方式 1 存  2 取"))
	if mode == 2:

		myMoney   = int(input("请输入取款金额"))
		if  money >= myMoney:
			print("取款:%d,余额:%d"%(myMoney,money-myMoney))
		else:
			print("没钱取毛线")
	if mode == 1:
		save =int(input("请输入存款金额"))
		print("余额：%d"%(money+save))
elif myAccount != account and myPasswd != passwd:
	print("帐号或密码错误")

