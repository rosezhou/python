class MusicPlayer(object):
	instance = 	None
	def __new__(cls):

		if cls.instance == None:
			cls.instance = super().__new__(cls)
			return cls.instance

	def __init__(self):

		print("天王盖地虎")


a = MusicPlayer()
b = MusicPlayer()
c = MusicPlayer()
print(id(a))
print(id(b))
print(id(c))
