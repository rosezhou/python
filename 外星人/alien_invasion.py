import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

	#初始化游戏窗口
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("外星人入侵")

	#设置背景颜色
	bg_color = (180,180,180)

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	
	#创建一个用于储存子弹的编组
	bullets = Group()

	#开始游戏的主循环
	while True:
		
		#鼠标键盘监听事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()

		#每次循环时都重绘屏幕
		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,ship,bullets)




run_game()