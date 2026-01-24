# Procedural approach

def checkEven(No):
	return(No % 2 == 0)
		

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