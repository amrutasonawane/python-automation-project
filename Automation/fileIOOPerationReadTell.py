def main():
	try:
		fobj = open("Hello.txt","r") #read file
		print("File get successfully open")
		
		print("Current obset : ", fobj.tell())
		data = fobj.read(6)
		print("Current offset : ", fobj.tell())
		
		print("Data in file in : ", data)

		fobj.close()


	except FileNotFoundError :
		print("Unable to open file as there no such file")
	finally :
		print("End of application")


if __name__ == "__main__":
	main()