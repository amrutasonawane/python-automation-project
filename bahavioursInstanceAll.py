class Demo:
	No=10

	def __init__(self,A,B):
		self.value1 = A
		self.value2 = B

#no decorater
	def fun(self):
		print("Inside instance method fun()",self.value1, self.value2)

#Compulsary decorator
	@classmethod
	def sun (cls):
		print("Inside class method sun()",cls.No)

#optional decorator but as per python doc, they are recommending to add decorator
	@staticmethod
	def gun():
		print("Inside static method gun()", Demo.No)

Demo.sun()
print("Class variable : ", Demo.No)
#Create object
obj1 = Demo(11,21)
obj1.fun()
print("Instance varibale : ", obj1.value1,obj1.value2)

Demo.gun()


