from functools import reduce

def checkEven(No):
	return (No % 2 == 0)

def increament(No):
	return No + 1

def Add(A,B) :
	return A + B

def main():
	Data = [11,10,15,20,22,27,30]
	print("Actual data is : ",Data)

	FData = list(filter(checkEven,Data))
	print("Filtered data is : ",FData)

	MData = list(map(increament,FData))
	print("Mapped data is : ",MData)

	Rdata = reduce(Add,MData)
	print("Reduce data is : ", Rdata)	


if __name__ == "__main__":
	main()