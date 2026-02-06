class Parent:
	def __init__(self):
		print("Inside parent class")
		self.no1 = 10
		self.no2 = 20

	def fun(self):
		print("Inside fun method of parent", self.no1,self.no2)

class Child(Parent):
	def __init__(self):
		super().__init__()
		print("Inside child contsructor")
		self.A =11
		self.B = 21

	def sun(self):
		print("Inside method sun of child", self.A,self.B,self.no1,self.no2) #11 21 10 20


cobj = Child() #memory get allocate to parent and then child

print(cobj.no1) #10
print(cobj.no2) #20

print(cobj.A) #11
print(cobj.B) #21

cobj.fun()
cobj.sun()

