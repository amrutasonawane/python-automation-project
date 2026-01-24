def Addition(*No):
	print(No)
	print(type(No)) #Tuple
	print(len(No))
	
def main():
	Addition(11,21)
	Addition(11,21,51,10)
	
if __name__ == "__main__":
	main()