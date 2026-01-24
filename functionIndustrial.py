# Procedural approach

def checkEven(No):
	if(No % 2 == 0):
		return True
	else:
		return False

def main() :
	value = 0
	value = int(input("Enter number : "))
	Result = checkEven(value)
	if(Result == True):
		print("It is even number")
	else:
		print("It is odd number")

if __name__ == "__main__" :
	main()