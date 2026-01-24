def summation(Arr):
	Sum = 0
	for i in range(len(Arr)):
			Sum = Sum + Arr[i]
	return Sum

	print("summation is : ", Sum)

def main():
	Value = 0
	
	size = int(input("Enter size of elements : "))
	Data = list()

	print("Enter the elements : ")

	for i in range(size):
		Value = int (input())
		Data.append(Value) # Data[i] = Value

	Result = summation(Data)
	print("Summation is : ",Result)


if __name__=="__main__" :
	main()