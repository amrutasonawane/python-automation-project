addition = lambda no1,no2 : no1+no2

subtraction = lambda no1,no2 : no1-no2

no1 = 0
no2 = 0
result = 0

no1 = int(input("Enter first number : ")) #11
no2 = int(input("Enter second number : ")) #10
result = addition(no1,no2)  #result = no1+no2   result = 11+10
print("Addition is : ", result)
result = subtraction(no1,no2) #result = no1-no2   result = 11-10
print("Subtraction is : ",result)