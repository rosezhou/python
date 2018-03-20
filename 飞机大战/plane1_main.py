import pygame
from plane2_sprites import *
from pygame.font import *
pygame.init()
pygame.mixer.music.load("/home/share/华语群星 - 奇迹再现.mp3")
pygame.mixer.music.play()


class PlaneGame(object):
	#游戏初始化
	def __init__(self):
		print("游戏初始化")
		#1 创建游戏初始化窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		#2 创建游戏时钟
		self.clock = pygame.time.Clock()
		#3 创建精灵和精灵组
		self.__create_sprites()
		#4 设置定时器事件，每秒创建一架敌机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#每隔0.5秒发射一颗子弹
		pygame.time.set_timer(HERO_FIRE_EVENT,300)
		# 英雄生命
		self.life1 = 1
		self.life2 = 1
		#初始分数
		self.score1 = 0
		self.score2 = 0


	#创建精灵组
	def __create_sprites(self):
		#第一个英雄
		self.hero = Hero()
		#第二个英雄
		self.newhero = NewHero()

		# #通过Hero类 实例第二个英雄
		# self.newhero = Hero()
		# self.rect.left = SCREEN_RECT.left - 50
		# self.rect.bottom = SCREEN_RECT.bottom
		#背景精灵
		bj1 = Background()
		bj2 = Background(True)
		self.back_groud = pygame.sprite.Group(bj1,bj2)

		#敌机精灵
		self.enemy_group = pygame.sprite.Group()

		#英雄组
		self.hero_group = pygame.sprite.Group(self.hero)
		self.newhero_group = pygame.sprite.Group(self.newhero)

	#开始游戏
	def start_game(self):
		print("开始游戏")
		while True:
			#设置刷新帧率
			self.clock.tick(60)	

			#事件监听
			self.__event_handler()

			#碰撞测试
			self.__check_collide()

			#更新精灵组
			self.__update_sprites()

			#显示得分板
			self.__print_score()

			#更新屏幕显示
			pygame.display.update()

	#事件监听
	def __event_handler(self):
		#退出
		for event in pygame.event.get():
			print(event)
			keys_pressed = pygame.key.get_pressed()


			if event.type == pygame.QUIT:
				game.__game_over()

			#英雄发射子弹
			elif event.type == HERO_FIRE_EVENT:
				self.newhero.fire()

			#敌机出场
			if event.type == CREATE_ENEMY_EVENT:
				print("敌机出场")
				self.enemy_group.add(Enemy())
			#空格发射子弹	
			elif keys_pressed[pygame.K_SPACE]:
				self.hero.fire()
		#操控
			#右
			elif keys_pressed[pygame.K_RIGHT]:
				self.hero.speeedx = 5
			elif keys_pressed[pygame.K_d]:
				self.newhero.speeed = 5
			#左
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speeedx = -5
			elif keys_pressed[pygame.K_a]:
				self.newhero.speeed = -5
			#上
			elif keys_pressed[273]:
				self.hero.speeedy = -5
			elif keys_pressed[pygame.K_w]:
				self.newhero.speeedz = -5
			#下
			elif keys_pressed[274]:
				self.hero.speeedy = 5
			elif keys_pressed[pygame.K_s]:
				self.newhero.speeedz = 5

			else:
				self.hero.speeedy = 0
				self.hero.speeedx = 0

				self.newhero.speeed = 0
				self.newhero.speeedz = 0
 
		


	#碰撞测试
	def __check_collide(self):

		#1 子弹摧毁敌机
		if pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True):
			self.score1 +=1
		if pygame.sprite.groupcollide(self.newhero.bullets2,self.enemy_group,True,True):
			self.score2 +=1
		#2 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		enemies2 = pygame.sprite.spritecollide(self.newhero,self.enemy_group,True)
		if len(enemies) > 0:
			self.life1 -= 1
			self.hero.rect.x = 1000	
			self.hero.rect.y = -1000
			self.hero.kill() 
		if len(enemies2) > 0:
			self.life2 -= 1
			self.newhero.rect.x = 1000
			self.newhero.rect.y = -1000
			self.newhero.kill()
		
		if self.life1 == 0 and self.life2 == 0 :
			PlaneGame.__game_over()
	def __print_score(self):
		"""显示得分"""
		pygame.font.init()
		pos1 = (200,0)
		pos2 = (600,0)
		color = (0,0,0)
		text1 = "SCORE1: " + str(self.score1)
		text2 = "SCORE2: " + str(self.score2)
		cur_font = pygame.font.SysFont("楷体",20)
		text_font1 = cur_font.render(text1,1,color)
		text_font2 = cur_font.render(text2,1,color)

		self.screen.blit(text_font1,pos1)
		self.screen.blit(text_font2,pos2)
	def __update_sprites(self):
		
		for group in [self.back_groud,self.enemy_group,self.hero_group,self.newhero_group,self.hero.bullets,self.newhero.bullets2]:

			group.update()
			group.draw(self.screen)


	@staticmethod
	def __game_over():
		print("游戏结束")

		pygame.quit()
		exit()
		
		

if __name__ == "__main__":
	game = PlaneGame()
	game.start_game()






