import threading

#Here display in callbackfunction, as we are not called it explicitly
def display():
	print("Inside display function :", threading.get_ident())

def main():
	print("Inside main : ", threading.get_ident())
	t = threading.Thread(target=display) # thread get create
	t.start()
	print("End of main")
	

if __name__ == "__main__":
	main()