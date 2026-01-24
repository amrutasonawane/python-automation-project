def main():
	result = 0
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	
	try :
		print("Inside try")
		result = no1/no2
	except:
		print("Inside except")

	print("Division is : ", result)

if __name__ == "__main__":
	main()