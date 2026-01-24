def main():
	Value = 0
	Sum = 0
	size = int(input("Enter size of elements : "))
	Data = list()

	print("Enter the elements : ")

	for i in range(size):
		Value = int (input())
		Data.append(Value) # Data[i] = Value

	for i in range(size):
			Sum = Sum + Data[i]

	print("summation is : ", Sum)


if __name__=="__main__" :
	main()