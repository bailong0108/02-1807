class Dog():
	def __init__(self):
		self.name =""
		self.__age = 0
	def sleep(self):
		print("sleep")
	def setAge(self,age): 
		if age > 15 or age < 1:
			print("年龄不符合")
		else:
			self.__age =age
	def getAge(self):
		return self.__age
hashiqi =Dog()
hashiqi.setAge(100)
#print(hashiqi.getAge()) #以前获取
#hashiqi.setAge(100)
print(hashiqi.getAge()) #现在获取
