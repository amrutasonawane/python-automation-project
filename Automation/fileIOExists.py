import os

def main():
	fileName = input("Enter name of file : ")

	ret = os.path.exists(fileName)

	if(ret==True):
		fobj = open(fileName,"r")
		print("file gets successfully open")
	else:
		print("There is no such file")


if __name__ == "__main__":
	main()