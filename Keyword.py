def EmployeeInfo(Name,Age, Salary,City):
	print("Name : ",Name)	
	print("Age : ",Age)	
	print("Salary : ",Salary)	
	print("City : ",City)	
	
def main():
	#Positional
	EmployeeInfo("Rahul",30,100000.50,"Pune") # Correct
	EmployeeInfo(30,"Rahul","Pune",100000.50) # Wrong
	
	#Keyword
	EmployeeInfo(Age=30,Name="Rahul",City="Pune",Salary=100000.50) #Correct
	
if __name__ == "__main__":
	main()