def EmployeeInfo(Name,Age, Salary,City="Pune"):
	print("Name : ",Name)	
	print("Age : ",Age)	
	print("Salary : ",Salary)	
	print("City : ",City)	
	
def EmployeeInfo1(Name="Amruta",Age=64, Salary=500000,City="Pune"):
	print("Name : ",Name)	
	print("Age : ",Age)	
	print("Salary : ",Salary)	
	print("City : ",City)	
	
def main():
	#Keyword
	EmployeeInfo(Age=30,Name="Rahul",City="Mumbai",Salary=100000.50) #Correct #default
	EmployeeInfo(Age=30,Name="Rahul",Salary=100000.50) # Keyword #dafult
	#EmployeeInfo("Rahul",30,100000.50) 
	EmployeeInfo1()
	
if __name__ == "__main__":
	main()