class Game(object):

	top_score = 99

	@staticmethod
	def show_help():
		print("欢迎来到召唤师峡谷")

	@classmethod
	def show_top_score(cls):
		print("当前最高分:"+str(cls.top_score))

	def __init__(self,name):
		
		self.player_name = name

	def star_game(self):
		print("开始游戏")

zhang_san = Game("张三")
Game.show_help()
Game.show_top_score()
zhang_san.star_game()
