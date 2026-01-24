
def factorial(no) :
	fact = 1
	for i in range (1,no+1):
		fact = fact * i
	return fact

def main():
	value = int (input("Enter number : "))
	ret = factorial(value)
	print("Factorial of given number is :", ret)

if __name__ == "__main__":
	main()