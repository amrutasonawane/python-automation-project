class Demo:
	No=11

	def __init__(self,A,B):
		self.value1 = A
		self.value2 = B

	def fun(self):
		print("Inside instance method fun()",self.value1, self.value2)

	@classmethod
	def sun (cls):
		print("Inside class method sun()",cls.No)

Demo.sun()
print("Class variable : ", Demo.No)
#Create object
obj1 = Demo(11,21)
obj1.fun()
print("Instance varibale : ", obj1.value1,obj1.value2)


