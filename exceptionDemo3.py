def main():
	result = 0
	try :
		print("Inside try")
		no1 = int(input("Enter first number : "))
		no2 = int(input("Enter second number : "))
		result = no1/no2

	except ValueError as vobj:
		print("Inside except : ", vobj)

	except ZeroDivisionError as zobj:
		print("Inside except : ",zobj)

	except Exception as eobj:
		print("Inside except : ",eobj)

	finally:
		print("Inside finally")

	print("Division is : ", result)

if __name__ == "__main__":
	main()