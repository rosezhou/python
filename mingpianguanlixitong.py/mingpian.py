
#名片管理系统
system = "名片管理系统"
print(system.center(50,"*"))
list = []

def print_add():
	message = {}
	name = input("请输入姓名\t")
	age = int(input("请输入年龄\t"))
	post = input("请输入职位\t")
	email = input("请输入邮箱\t")
	tel = int(input("请输入手机号\t"))
	isrepeat = False
	for info in list:
		for key in info:
			if info.get(key) == name:
				print("用户已经存在，请从新输入")
				print("*"*50)
				isrepeat = True
				break
	if not isrepeat:
		message["姓名"] = name
		message["年龄"] = age
		message["职位"] = post
		message["电话"] = tel
		list.append(message)
		print("操作成功")
		print("*"*50)



def print_del():
	card == 2#删除选项
	delete = input("请选择需要删除的用户\t")
	for i in list:
		if i["姓名"]  == delete:
			list.remove(i)
			print("你已成功删除%s"%delete)
			print("*"*50)
		else:
			print("系统没有此人")
			print("*"*50)


def print_change():
	card == 3#修改选项
	alter = input("请输入需要修改的用户:")
	for z in list:
		if z["姓名"] == alter:
			while True:
				me = input("请输入需要修改的项 1 姓名 2 年龄 3 职位 4 电话 5 退出")
				if me == "1":
					my = input("请输入需要变更的名字:\t")
					z["姓名"] = my
					print("你已经成功修改为: %s"%my)
					print("*"*50)
				elif me == "2":
					year = int(input("请输入需要变更的年龄:\t"))
					z["年龄"] = year
					print("你已经成功修改年龄为 :%d"%year)
					print("*"*50)
				elif me == "3":
					job = input("请输入需要变更的职位:\t")
					z["职位"] = job
					print("你已经成功修改职位为 :%s"%job)
					print("*"*50)
				elif me == "4":
					number = int(input("请输入需要变更的电话:\t"))
					z["电话"] = number
					print("你已经成功修改电话为: %d"%number)
					print("*"*50)
				elif me =="5":
						break
			else:
				print("你输入的有误")
				print("*"*50)


def print_find():
	card == 4#查找选项
	find = input("请输入需要查找的用户:\t")
	for q in list:
		if q["姓名"] == find:
			for y in q:
				print(y,q[y])
				print("*"*50)
		if q["姓名"] != find:
			print("系统没有此人")
			print("*"*50)

	


while True:

	card = int(input("请输入需要服务的项目 1 添加 2 删除 3 修改 4 查询 5 退出"))

	if card == 1:
		print_add()

	if card == 2: 
		print_del()

	if card == 3:
		print_change()

	if card == 4:
		print_find()

	if card == 5:
		break
	for i in list:
		print(i)
