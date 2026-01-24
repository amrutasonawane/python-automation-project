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
	t1 = threading.Thread(target=sumEven,args=(100000000,))
	t2 = threading.Thread(target=sumOdd,args=(100000000,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	end_time = time.time()

	print("Time require : ", end_time-start_time)

if __name__ == "__main__":
	main()