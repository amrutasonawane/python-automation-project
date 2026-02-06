import os

def main():
	fileName = input("Enter name of file : ")

	if(os.path.exists(fileName)):

		ret = os.path.isabs(fileName) # isabs = it is blind method

		if(ret == True):
			print("It is absolute path")
		else:
			print("It is relative path")
			newpath = os.path.abspath(fileName) #abspath = it is blind function
			print("Updated path : ",newpath)
	else :
		print("There is no such file")


if __name__ == "__main__":
	main()