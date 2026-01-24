from functools import reduce

#checkEven =  lambda No : (No % 2 == 0)
#increament = lambda No : No + 1
#Add = lambda A,B : A + B

def main():
	Data = [11,10,15,20,22,27,30]
	print("Actual data is : ",Data)

	FData = list(filter(lambda No : (No % 2 == 0)),Data)
	print("Filtered data is : ",FData)

	MData = list(map((lambda No : No + 1),FData))
	print("Mapped data is : ",MData)

	Rdata = reduce((lambda A,B : A + B),MData)
	print("Reduce data is : ", Rdata)	


if __name__ == "__main__":
	main()