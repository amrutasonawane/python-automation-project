import hashlib
import os

def calculateChecksum(fileName): #4567 byte
	fobj = open(fileName,"rb")
	hobj = hashlib.md5()

	buffer = fobj.read(1000)

	while(len(buffer) > 0):
		hobj.update(buffer)
		buffer = fobj.read(1000)

	fobj.close()
	return hobj.hexdigest()

def directoryWatcher(directoryName = "Marvellous"):
	ret =False
	ret = os.path.exists(directoryName)
	if (ret == False) :
		print("There is no such directory")
		return
	ret = os.path.isdir(directoryName)
	if(ret == False):
		print("It is not a directory")
		return
	for FolderName, subfolderName, FileName in os.walk(directoryName):
		for fname in FileName : 
			fname = os.path.join(FolderName,fname)
			print("File name after joiing is : ",fname)
			checkSum = calculateChecksum(fname)
			print(f"File name :{fname} Checksum : {checkSum}")

def main():
	directoryWatcher()

if __name__ == "__main__":	
	main()