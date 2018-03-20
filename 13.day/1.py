class Gun(object):

	def __init__(self,model):
		self.model = model

		self.bullet_count = 0

	def add_bullet(self,count):
		self.bullet_count += count

	def shoot(self):
		if self.bullet_count <= 0:
			print("没有子弹了")
			return

		else:
			print(self.model + "发射了" + str(self.bullet_count) + "颗子弹...!")


ak47 = Gun("ak47")
ak47.add_bullet(30)
ak47.shoot()