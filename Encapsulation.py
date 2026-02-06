#Encapsulation is bidning of charteristics and bahaviouer together
class Arithmatic:
	def __init__(self,A,B):
		self.no1 = A #characteristics
		self.no2 = B	
		print("Object get created successfully")

	def addition(self):
		Ans = 0
		Ans =self.no1 + self.no2
		return Ans

	def subtraction(self):
		Ans = 0
		Ans =self.no1 - self.no2
		return Ans







obj1 = Arithmatic(11,10) #Arithmatic(id(obj1),11,10) -> __init__(id(obj1),11,10)
obj2 = Arithmatic(21,20)

result = obj1.addition()
print(result)

result = obj2.subtraction() #subtraction(id(obj2),21,20)
print(result)