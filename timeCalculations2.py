import time

def factorial(no) :
	fact = 1
	for i in range (1,no+1):
		fact = fact * i
	return fact

def main():
	value = int (input("Enter number : "))
	start_time = time.time()
	ret = factorial(value)
	end_time = time.time()
	print("Factorial of given number is :", ret)
	print("Total time require for execution : ", end_time-start_time)

if __name__ == "__main__":
	main()