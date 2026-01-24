import multiprocessing
import time
import os

def sumEven(no):
	print("PID of sumEve() : ", os.getpid()) # 51
	print("PPID of sumEve() : ", os.getppid()) # 21
	sum = 0
	for i in range(2,no+1,2):
		sum = sum + i
	print("Summation of even number is : ",sum)

def sumOdd(no):
	print("PID of sumOdd() : ", os.getpid()) #101
	print("PPID of sumOdd() : ", os.getppid()) # 21
	sum = 0
	for i in range(1,no+1,2):
		sum = sum + i
	print("Summation of even number is : ",sum)



def main():
	print("PID of main() : ", os.getpid()) # self 21
	print("PPID of main() : ", os.getppid()) #cmd 11
	start_time = time.time()
	t1 = multiprocessing.Process(target=sumEven,args=(100000000,))
	t2 = multiprocessing.Process(target=sumOdd,args=(100000000,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	end_time = time.time()

	print("Time require : ", end_time-start_time)

if __name__ == "__main__":
	main()