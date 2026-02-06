import os

def directoryScanner(DirectoryName =  "Marvellous"):
	Ret = os.path.exists(DirectoryName)

	if(Ret == False):
		print("There is no such directory")
		return

	Ret = os.path.isdir(DirectoryName)
	if(Ret ==  False):
		print("Uanble to scan as its a not a directory")
		return
	
	print("Contents under directry are : ")
	for FolderName , SubFolderName , FileName in os.walk(DirectoryName) : 
		print("Folder name is :",FolderName)

		for subf in SubFolderName :
			print("Subfolder name : ",subf)

		for fname in FileName:
			print("file name : ",fname)

def main():
	DirectoryName  = input("Enter name of directory : ") #Directory is treated as special file
	if(os.path.exists(DirectoryName)) : 
		directoryScanner(DirectoryName)

if __name__ == "__main__":
	main()