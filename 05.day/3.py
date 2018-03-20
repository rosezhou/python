def message():
	list = []
	while True:
		name = {}
		names = input("请输入姓名: ")
		age = int(input("请输入年龄: "))
		isrepeat = 	False
		for info in list:
			for key in info:
				if info.get(key) == names:
					print("用户已经存在，请重新输入")
					isrepeat = True
					break
		if not isrepeat:

			name["names"] = names
			name["age"] = age 
			list.append(name)
			for i in list:
				for j in i :
					print(j,i[j])
		
				
message()
	
