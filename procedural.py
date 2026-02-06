def addition(no1,no2):
	return no1+no2

def subtraction(no1,no2):
	return no1-no2

no1 = 0
no2 = 0
result = 0

no1 = int(input("Enyer first number : "))
no2 = int(input("Enter second number : "))
result = addition(no1,no2)
print("Addition is : ", result)
result = subtraction(no1,no2)
print("Subtraction is : ",result)