class showError(Exception):
	def __init__(self,name):
		self.name = name

class InputManger():
	def my_input(self):
		self.name = input("请输入名字")
		try:
			if self.name == "laowang":
				raise showError(self.name)
		except showError as ret:
			print("错误")
im = InputManger()
im.my_input()
