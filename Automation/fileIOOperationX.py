def main():
	try:
		open("demo.txt","r")
		print("File get successfully open")
	except FileNotFoundError :
		print("Unable to open file as there no such file")
	finally :
		print("End of application")



if __name__ == "__main__":
	main()