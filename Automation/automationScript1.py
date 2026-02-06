import sys
def main():
	Border = "-"*40
	print(Border)
	print("---------Marvellous automation----------")
	print(Border)

	if(len(sys.argv)== 2):
		if((sys.argv[1]== "--h") or (sys.argv[1] == "--H")):
			print("this application is used to perform ---")
			print("This is automation script")
		elif((sys.argv[1]== "--u") or (sys.argv[1] == "--U")):
			print("Use the given script as ")
			print("ScriptName.py Argument1 Argument2")
			print("Argument1 : ___________")
			print("Argument2 : ___________")
		else:
			print("Use valid flags as : ")
			print("--u : User to display usage")
			print("--h : User to display help")
	else:
			print("Invalid number of command line arguments")
			print("Use valid flags as : ")
			print("--u : User to display usage")
			print("--h : User to display help")

	print(Border)
	print("-----Thank you for using our script-----")
	print("---------Marvellous Infosystems---------")
	print(Border)

if __name__ == "__main__":
	main()