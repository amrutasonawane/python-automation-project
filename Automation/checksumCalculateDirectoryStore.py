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

def findDuplicate(directoryName = "Marvellous"):
	ret =False
	ret = os.path.exists(directoryName)
	if (ret == False) :
		print("There is no such directory")
		return
	ret = os.path.isdir(directoryName)
	if(ret == False):
		print("It is not a directory")
		return
	duplicate = {}
	for FolderName, subfolderName, FileName in os.walk(directoryName):
		for fname in FileName : 
			fname = os.path.join(FolderName,fname)
			checkSum = calculateChecksum(fname)
			#print(f"File name :{fname} Checksum : {checkSum}")
			if(checkSum in duplicate):
				duplicate[checkSum].append(fname)
			else :
				duplicate[checkSum] = [fname]
	return duplicate

def displayResult(mydict):
		count=0
		result = list(filter(lambda x : len(x)>=1, mydict.values()))
		for value in result:
			for subvalue in value:
				count = count + 1
				print(subvalue)
			print("Value of count : ", count)
			count = 0

def deleteDuplicate(path = "Marvellous"):
	mydict = findDuplicate(path)
	count=0
	cnt = 0
	result = list(filter(lambda x : len(x)>=1, mydict.values()))
	for value in result:
		for subvalue in value:
			count = count + 1
			if(count > 1):
				print("Deleted file",subvalue)
				os.remove(subvalue)
				cnt = cnt + 1
		count = 0
	print("Total deleted files : ",cnt)


def main():
	deleteDuplicate()


if __name__ == "__main__":	
	main()