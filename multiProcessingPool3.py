import time
import os

def sumCube(no1):
	print("Process is running with pid : ", os.getpid())
	sum=0
	for	i in range (1,no1+1):
		sum = sum + (i**3)
	return sum

def main():
	data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
	result = []
	start_time =  time.time()
	for i in range(len(data)):
		result.append(sumCube(data[i]))

	end_time = time.time()	
	print("summation is : ",result)
	print("Total time is : ", end_time-start_time)

if __name__ == "__main__":
	main()