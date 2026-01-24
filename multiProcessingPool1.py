def sumCube(no1):
	sum=0
	for	i in range (1,no1+1):
		sum = sum + (i*i*i)
	return sum

def main():
	result = 	sumCube(10)
	print("summation is : ",result)

if __name__ == "__main__":
	main()