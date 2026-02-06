import os

def main():
	fileName = input("Enter name of file : ")

	if(os.path.exists(fileName)):
		os.remove(fileName)
		print("File gets deleted")
	else:
		print("File not exists")

if __name__ == "__main__":
	main()