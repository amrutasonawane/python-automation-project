class Parent:
	def __init__(self):
		print("Inside parent class")
		self.no1 = 10
		self.no2 = 20

	def fun(self):
		print("Inside fun method of parent")

class Child(Parent):
	def __init__(self):
		super().__init__()
		print("Inside child contsructor")
		self.A =11
		self.B = 21

	def sun(self):
		print("Inside method sun of child")


cobj = Child() #memory get allocate to parent and then child