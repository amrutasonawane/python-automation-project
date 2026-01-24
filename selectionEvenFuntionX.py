# Procedural approach

def checkEven(no):
	if(no % 2 == 0):
		print("it is Even number")
	else:
		print("It is odd number")

def main() :
	value = 0
	value = int(input("Enter number : "))
	Result = checkEven(value)

if __name__ == "__main__" :
	main()