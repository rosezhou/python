
list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":123123,"renkou":123123}}]
for i in list:
	
	for z in i :

		for q in i[z]:
			print(z,q,i[z][q])

