import os
import sys

def directoryScanner(dirName = "Marvellous"):
	ret = False
	ret = os.path.exists(dirName)
	if(ret == False):
		print("There is no such directory")
		return
	ret = os.path.isdir(dirName)
	if(ret == False):
		print("It is not a directory")
		return
	fileCount = 0
	emptyFileCount = 0
	for folderName, subfolderName,fileName in os.walk(dirName):
		for fname in fileName :
			fileCount = fileCount + 1
			fname = os.path.join(folderName,fname)
			print("File name : ",fname)
			print("File size : ",os.path.getsize(fname))
			if(os.path.getsize(fname) == 0):
				emptyFileCount = emptyFileCount + 1
				os.remove(fname)
	Border = "_"*50
	print(Border)
	print()
	print("------------Automation Report----------")
	print()
	print("Total file scanned :",fileCount)
	print("Total empty file found : ",emptyFileCount)
	print(Border)



def main():
	Border = "_"*50
	print(Border)
	print()
	print("----------Marvellous Directory Automation---------")
	print(Border)

	if(len(sys.argv) !=2):
		print("Invalid number if argumanets")
		print("Please specify name of directory")
		return
	else:
		directoryScanner(sys.argv[1])
	Border = "_"*50
	print(Border)
	print()
	print("----------Marvellous Directory Automation---------")
	print(Border)


if __name__ == "__main__":
	main()