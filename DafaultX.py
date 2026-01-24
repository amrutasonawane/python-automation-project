def EmployeeInfo(Name,Age, Salary,City="Mumbai"):
	print("Name : ",Name)	
	print("Age : ",Age)	
	print("Salary : ",Salary)	
	print("City : ",City)	

	
def main():
	EmployeeInfo("Rahul",30,100000.50) # Dafult
	EmployeeInfo("Rahul",30,100000.50,"Pune") # Dafult
	
if __name__ == "__main__":
	main()