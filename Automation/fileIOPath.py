import os

def main():
	fileName = input("Enter name of file : ")

	ret = os.path.isabs(fileName)

	if(ret == True):
		print("It is absolute path")
	else:
		print("It is relative path")

if __name__ == "__main__":
	main()