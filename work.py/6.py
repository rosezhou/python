for i in range(2,101):
	d = 0
	for z in range(2,i):
		if i%z == 0:
			d = 1
			break
	if d == 0:
		print(i)
