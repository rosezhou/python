title = "个人信息管理系统"
print(title.center(30,"*"))

name = []

lecect = int(input("请选择功能1新增 2查询 3修改 4删除"))
if lecect == 1:
	m = input("请输入姓名\t")
	age = int(input("请输入年龄\t"))
	sex = input("请输入性别\t")
	work = input("请输入工作\t")
	name.append(m)
	name.append(age)
	name.append(sex)
	name.append(work)
	print(name)
elif lecect == 2:
	inquire = int(input("请输入索引:\t"))
	print(name[inquire])
elif lecect == 3:
	name = input("请输入姓名\t:")
	newName = input("请输入新的姓名:\t")
	list[0] = newName
	print(name)
elif lecect == 4:
	delete = input("请输入你要删除的人名:\t")
	list.remove(delete)
	print(name)
