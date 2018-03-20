#小游戏：石头简单布

import random
computer =random.randint(1,3)
me = int(input("请输入:1 石头，2 剪刀,3 布，\t"))
if me <= 3 and me > 0:
	if (me == 1 and computer == 2) or (me == 2 and computer == 3) or (me == 3 and computer == 1 ): 
		print("恭喜，您赢了")
	elif (me == computer):
		print("不输不赢，战成平手")
	else:
		print("不好意思,我赢了")
else:
	print("你走吧，不让你玩了")
