import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,700,480)

CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_name,speeed=1):

		super().__init__()

		#加载图像
		self.image = pygame.image.load(image_name)

		#设置尺寸
		self.rect = self.image.get_rect()

		#记录速度
		self.speeed = speeed
		

		
	def update(self,*args):
	 	#垂直向下移动
	 	self.rect.x -= self.speeed



class Background(GameSprite):
	"""背景精灵"""
	
	def __init__(self,is_alt = False):
		
		super().__init__("./images/background.png")
		if is_alt:
			self.rect.x = self.rect.width

	def update(self):
		super().update()
		if self.rect.x == -SCREEN_RECT.width:
			self.rect.x = self.rect.width



class Enemy(GameSprite):
	"""敌机精灵"""


	def __init__(self):
		#调用父类方法，创建敌机精灵，载入图片
		super().__init__("./images/enemy1.png")

		#设置敌机的随机初始速度
		self.speeed = random.randint(2,4)

		#设置敌机的初始化位置
		self.rect.x = SCREEN_RECT.width

		max_x = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(0,max_x)


	def update(self):
		super().update()
		if self.rect.x <= 0:
			print("敌机飞出屏幕了")
			self.kill()



class Hero(GameSprite):
	"""英雄精灵"""

	def __init__(self):
		super().__init__("./images/life.png",0)
		#设置英雄初始位置
		self.rect.y = 50
		self.rect.x = 0

		#子弹精灵组
		self.bullets = pygame.sprite.Group()



	def update(self):
		self.rect.x += self.speeedx
		self.rect.y += self.speeedy

	
		
		if self.rect.left < 0:
			self.rect.left = 0
	
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
	
		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom

	def fire(self):

		for i in (1,2,3):
			bullet = Bullet()

			bullet.rect.x = self.rect.width+self.rect.x + 20*i
			bullet.rect.centery = self.rect.centery

			#将子弹精灵添加到精灵组
			self.bullets.add(bullet)

class NewHero(GameSprite):
	"""第二个英雄"""

	def __init__(self):
		super().__init__("./images/life.png",0)
		self.rect.left = SCREEN_RECT.left
		self.rect.bottom = SCREEN_RECT.bottom - 50

				#子弹精灵组
		self.bullets2 = pygame.sprite.Group()

	def update(self):

		self.rect.x += self.speeed
		self.rect.y += self.speeedz


				#控制英雄边界 屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0

		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom

	def fire(self):

		for i in (1,2,3):
			bullet2 = Bullet()

			bullet2.rect.x = self.rect.right + 20*i
			bullet2.rect.centery = self.rect.centery

			#将子弹精灵添加到精灵组
			self.bullets2.add(bullet2)





class Bullet(GameSprite):
	"""子弹精灵"""
	def __init__(self):
		super().__init__("./images/bullet1.png",-8)

	def update(self):

		super().update()
		#判断子弹是否飞出屏幕
		if self.rect.x > SCREEN_RECT.width:
			self.kill()

