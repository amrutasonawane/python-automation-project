import os
import sys
import time
import schedule

def directoryScanner(dirName = "Marvellous"):
	Border = "_"*50
	timeStamp =time.ctime()
	logFileName = "Marvellous %s.log" %(timeStamp)
	logFileName = logFileName.replace(" ","_")
	logFileName = logFileName.replace(":","_")
	fobj = open(logFileName,"w")
	fobj.write(Border +"\n")
	fobj.write("This is log file created by Marvellous automation"+"\n")
	fobj.write("This is a directory cleaner script"+"\n")
	fobj.write(Border +"\n")
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
			#print("File name : ",fname)
			#print("File size : ",os.path.getsize(fname))
			if(os.path.getsize(fname) == 0):
				emptyFileCount = emptyFileCount + 1
				os.remove(fname)

	fobj.write(timeStamp+" Total file scanned :"+ str(fileCount) + "\n")
	fobj.write(timeStamp+" Total empty file found : "+ str(emptyFileCount) + "\n")
	fobj.write("This log file created at : "+ timeStamp+"\n")
	fobj.write(Border +"\n")

	fobj.close()


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

	#directoryScanner(sys.argv[1])

	schedule.every(1).minute.do(directoryScanner)

	while(True):
		schedule.run_pending()
		time.sleep(20)

	Border = "_"*50
	print(Border)
	print()
	print("----------Marvellous Directory Automation---------")
	print(Border)


if __name__ == "__main__":
	main()