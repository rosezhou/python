#电影院自主系统
print("自助售票机".center(30,"-"))

#我的帐号
account = "123456"
pwd     = "321123"


list = []
#登录操作
def print_login():
	while True:
		login = int(input("1 新用户 2 老用户 3 退出"))
		if login == 1 :
			message = {}
			name = input("请输入姓名\t")
			age  = input("请输入年龄\t")
			sex  = input("请输入性别\t")
			ID_number = input("请输入证件号\t")
			message["name"]   = name
			message["age"]    = age
			message["sex"]    = sex
			message["ID_num"] = ID_number
			list.append(message)
			print("注册成功")
			for z in list:
				for k,v in z.items():
					print(k,v)
			handle()


		if login == 2:
			myAccount = input("请输入帐号\t")
			myPwd       = input("请输入密码\t")
			if myAccount == account and myPwd == pwd:
				print("登录成功")
				handle()
			else:
				print("登录失败")

		elif login == 3:
			break

#登录成功后的操作
def handle():
	fare = [{"前任三":35},{"芳华":30},{"二代妖精":38}]
	while True:
		option = int(input("1 查询 2 购买 3 退出"))
		if option == 1:
			for j in fare:
				for k,v in j.items():
					print(k,v)

		elif option == 2:
			buy = input("请输入要购买的电影")
			for z in fare:
				for k,v in z.items():
					if buy == k:
						my = int(input("请输入付款金额"))
						print("你付款%d找零%.2f,欢迎下次光临"%(my,my-z[buy]))
		elif option == 3:
			break


print_login()
