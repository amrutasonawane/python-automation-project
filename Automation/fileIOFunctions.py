import os

def main():
	fileName = input("Enter name of file : ")

	if(os.path.exists(fileName)): 
		fobj = open(fileName,"r")
		print(fobj.name)  #Demo.txt
		print(fobj.mode)#r
		print(fobj.closed)#False

		fobj.close()
		print(fobj.closed)#True
	else:
		print("File not exists")

if __name__ == "__main__":
	main()