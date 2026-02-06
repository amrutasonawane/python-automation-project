def main():
	try:
		fobj = open("Hello.txt","r") #read file
		print("File get successfully open")
		
		data = fobj.read(6)
		fobj.close()

		print("Data in file in : ", data)

	except FileNotFoundError :
		print("Unable to open file as there no such file")
	finally :
		print("End of application")



if __name__ == "__main__":
	main()