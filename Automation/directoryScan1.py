import os 

def main():
	DirectoryName  = input("Enter name of directory : ") #Directory is treated as special file
	print("Contents under directry are : ")

	for FolderName , SubFolderName , FileName in os.walk(DirectoryName) : 
		print("Folder name is :",FolderName)

		for subf in SubFolderName :
			print("Subfolder name : ",subf)

		for fname in FileName:
			print("file name : ",fname)


if __name__ == "__main__":
	main()