import pygame


#初始化方法
pygame.init()


#创建游戏屏幕
screen = pygame.display.set_mode((480,700))


	
#绘制背景 加载图像
setting = pygame.image.load("./images/background.png")
#绘制在屏幕
screen.blit(setting,(0,0))

#创建英雄
heroman = pygame.image.load("./images/life.png")
#定义英雄初始位置
hero_rect = pygame.Rect(273,650,46,57)
#绘制在屏幕
screen.blit(heroman,hero_rect)

#刷新屏幕
pygame.display.update()

#创建游戏时钟对象
clock = pygame.time.Clock()


while True:
	"""
	clock.tick(60)
	
	hero_rect.y -= 1
	if hero_rect.y + hero_rect.height <= 0:
		hero_rect.y = 650
	hero_rect = pygame.Rect(273,hero_rect.y,46,57)
	screen.blit(heroman,hero_rect)
	pygame.display.update()
	"""	

	#事件监听
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			exit()

			
		if event.type == pygame.K_UP:
			hero_rect.y -= 5
			
			"""
			elif event.key == 274:
				hero_rect.y += 5
				
				

			elif event.key == 275:
				hero_rect.x += 5
				
				

			elif event.key == 276:
				hero_rect.x -= 5
			"""
		screen.blit(heroman,hero_rect)
		pygame.display.update()
#退出			
pygame.quit()
