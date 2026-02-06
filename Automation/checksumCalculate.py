import hashlib

def calculateChecksum(fileName): #4567 byte
	fobj = open(fileName,"rb")
	hobj = hashlib.md5()

	buffer = fobj.read(1000)

	while(len(buffer) > 0):
		hobj.update(buffer)
		buffer = fobj.read(1000)

	fobj.close()
	return hobj.hexdigest()


def main():
	checkSum = calculateChecksum("demo.txt")
	print("Checksum is : ",checkSum)

if __name__ == "__main__":	
	main()