def main():
	try:
		fobj = open("Hello.txt","a")
		print("File get successfully open")
		fobj.write("Python Automation....")
		fobj.close()

	except FileNotFoundError :
		print("Unable to open file as there no such file")
	finally :
		print("End of application")



if __name__ == "__main__":
	main()