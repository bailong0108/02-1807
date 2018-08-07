class Person:
	def eat(self):
		print("吃饭")
	def sleep(self):
		print("睡觉")
	def play(self):
		print("玩")
	def introduce(self):
		print("我年龄是%d 我的身高是%d"%(self.age,self.height))
bql =Person()
bql.eat()
bql.sleep()
bql.play()
bql.age=18 #添加属性
bql.height = 170 #添加属性
bql.introduce()
print(bql.age)
print(bql.height)

mry = Person()
mry.eat()
mry.sleep()
mry.play()
mry.age = 19 #添加属性
mry.height = 171 
mry.introduce()
