import threading
import time

def sumEven(no):
	sum = 0
	for i in range(2,no+1,2):
		sum = sum + i
	print("Summation of even number is : ",sum)

def sumOdd(no):
	sum = 0
	for i in range(1,no+1,2):
		sum = sum + i
	print("Summation of even number is : ",sum)



def main():
	start_time = time.time()
	sumEven(100000000)
	sumOdd(100000000)
	end_time = time.time()

	print("Time require : ", end_time-start_time)

if __name__ == "__main__":
	main()