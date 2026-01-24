from functools import reduce

checkEven = lambda No : (No % 2 == 0)
increament = lambda No : No + 1
Add = lambda A,B : A + B

def filterX(task,elements):
	Result = list()
	for no in elements : 
		ret = task(no)
		if(ret == True):
			Result.append(no)
	return Result

def mapX(task,elements):
	Result = list()
	for no in elements:
		Ret = task(no)
		Result.append(Ret)
	return Result

def reduceX(task,elements):
	sum = 0
	for no in elements:
		sum = task(sum,no)
	return sum

def main():
	Data = [11,10,15,20,22,27,30]
	print("Actual data is : ",Data)

	FData = list(filterX(checkEven,Data))
	print("Filtered data is : ",FData)

	MData = list(mapX(increament,FData))
	print("Mapped data is : ",MData)

	Rdata = reduceX(Add,MData)
	print("Reduce data is : ", Rdata)	


if __name__ == "__main__":
	main()