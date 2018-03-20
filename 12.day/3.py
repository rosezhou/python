class MusicPlayer(object):

	b = False
	a = None

	def __new__(cls):
		if cls.a is None:
			cls.a = super().__new__(cls)
		return cls.a

	def __init__(self):

		if self.b == True:
			return

		print("天王盖地虎")
		self.b = True

A = MusicPlayer()
B = MusicPlayer()
print(id(A))
print(id(B))