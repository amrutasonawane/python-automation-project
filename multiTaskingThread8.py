import threading

def display(no1, no2, no3):
	print("Inside display : ",no1,no2, no3)

def main():
	t = threading.Thread(target=display,args=(11,34,23)) #it is internally tuple
	t.start()
	

if __name__ == "__main__":
	main()