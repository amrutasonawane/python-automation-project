def main():
	Value = 0
	size = int(input("Enter size of elements : "))
	Data = list()

	print("Enter the elements : ")

	for i in range(size):
		Value = int (input())
		Data.append(Value)
	print(Data)

if __name__=="__main__" :
	main()