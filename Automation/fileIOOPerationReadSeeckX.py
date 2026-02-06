# seek (Kuthe, kuthun)
# Kuthun : 0/1/2
# 0 : Starting
# 1 : Current
# 2 : End

def main():
	try:
		fobj = open("Hello.txt","r") #read file
		print("File get successfully open")
		
		print("Current offset : ", fobj.tell()) #0

		fobj.seek(7,0)
		print("Current offset : ", fobj.tell()) #7

		data = fobj.read(10)
		print("Current offset : ", fobj.tell()) #17
		
		print("Data in file in : ", data)

		fobj.close()


	except FileNotFoundError :
		print("Unable to open file as there no such file")
	finally :
		print("End of application")


if __name__ == "__main__":
	main()