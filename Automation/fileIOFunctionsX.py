import os

def main():
	fileName = input("Enter name of file : ")

	if(os.path.exists(fileName)): 
		fobj = open(fileName,"w")
		
		print(fobj.readable())
		print(fobj.writable())
		print(fobj.seekable())

	else:
		print("File not exists")

if __name__ == "__main__":
	main()