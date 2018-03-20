class User(object):

	def __init__(self,first_name,last_name,age,sex):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex

	def describe_user(self):
		print(self.first_name,self.last_name,self.age,self.sex)

	def greet_user(self):
		print("Hello " + self.last_name + self.first_name + "!")
"""
xiaoming = User("明","小","17","男")
xiaoming.describe_user()
xiaoming.greet_user()

xiaohong = User("红","小","21","女")
xiaohong.describe_user()
xiaohong.greet_user()
"""

class Admin(User):

	def __init__(self):

		pass
	def show_privileges(self):
		privileges = ["can add post","can delete post","can ban User","can do like"]
		print("管理员的权限都有:" + str(privileges))
"""		
asdasd = Admin()
asdasd.show_privileges()
"""
class Privileges:


	privileges = ["can add post","can delete post","can ban User","can do like"]
	@classmethod
	def show_privileges(self):
		privileges = ["can add post","can delete post","can ban User","can do like"]
		print("管理员的权限都有:" + str(privileges))

a = Privileges()
a.show_privileges()

















