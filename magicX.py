#Dunder method / Magic method / Special method
class Demo:
	def __init__(self,A):
		self.No = A

	def __add__(self,other):
		print("Inside __add__")
		return self.No + other.No

	def __sub__(self,other):
		print("Inside __sub__")
		return self.No - other.No

	def __mul__(self,other):
		print("Inside __mul__")
		return self.No * other.No

	def __truediv__(self,other):
		print("Inside __truediv__")
		return self.No / other.No

obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2) #due to this + sign __add__ method get called #__add__(obj1,obj2)
print(obj1 - obj2) #__sub__(obj1,obj2)
print(obj1 * obj2) #__mul__(obj1,obj2)
print(obj1 / obj2) #__truediv__(obj1,obj2)