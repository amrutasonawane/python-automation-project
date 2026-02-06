class Demo: 
 #class variable
	No1 = 10
	No2 = 11

	def __init__(self): #To create instance variable we have to write constructor
		#Instance variable
		self.A = 101
		self.B = 201
		print("Inside Constructor")

	def __del__(self):
		print("Inside destructor")

print(Demo.No1)
print(Demo.No2)

obj = Demo()

print(obj.A)
print(obj.B)

