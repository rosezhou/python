class Toor(object):
	count = 0

	def __init__(self,name):
		self.name = name
		Toor.count += 1

	@classmethod				
	def tool_show_count(cls):
		print("创建了%d"%Toor.count)
		print("创建了%d"%cls.count)

gai_zhui = Toor("改锥")
luo_si_dao = Toor("螺丝刀")

Toor.tool_show_count()


"""
print(Toor.count)
print(gai_zhui.count)
print(luo_si_dao.count)
"""