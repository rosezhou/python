""
names = ["小明","小红","小刚","小强","小绿"]

for i in names:
	print(i)#二.1


for i in names:
	print("Hello,%s how are you!"%i)#二.2


trip = ("bike","roadser","mountain bike")
for i in trip:
	print("I would like to own a %s "%i)
"""

name = ["godzhou","rosezhou","jaczhou"]
for i in name:
	print("%s我们一起咪西咪西"%i)


#有一个嘉宾无法赴约，需要新来一位嘉宾
print("%s无法赴约"%name.pop())
name.append("moneyzhou")
print("欢迎刚来的新嘉宾%s"%name[-1])
for z in name:
	print("%s我们一起咪西咪西"%z)

new = input("请输入新来的嘉宾\t")
new1 = input("请输入第二位嘉宾\t")
new2 = input("请输入第三位嘉宾\t")
name.insert(0,new)
name.insert(1,new1)
name.append(new2)

print("因为换了一个大餐桌,我又邀请了三个嘉宾，分别是 %s, %s, %s"%(new,new1,new2))
for p in name :
	print("%s让我们来咪西咪西"%p)
