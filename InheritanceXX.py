class Parent:
	def __init__(self):
		print("Inside parent class constructor")

	def fun(self):
		print("Inside fun method of parent")

class Child(Parent):
	def __init__(self):
		super().__init__()
		print("Inside child constructor")

	def fun(self):
		super().fun()
		print("Inside fun method of child")


cobj = Child() #memory get allocate to parent and then child
cobj.fun()
