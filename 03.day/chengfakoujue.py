count = 1
while count <= 9:
	z = 1
	while z <= count:
		print("%d*%d=%d"%(z,count,count*z),end="\t")
		z+=1
	print("")

	count+=1
