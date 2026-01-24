import os

def main():
	print("PID of running process id :", os.getpid())
	print("PID of parent process is: ", os.getppid())

if __name__ == "__main__":
	main()