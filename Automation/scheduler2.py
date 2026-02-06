import time
import datetime
import schedule


def fun():
	print("Inside Fun at : ", datetime.datetime.now())

def main():
	print("Inside marvellous automation script at : ", datetime.datetime.now())
	schedule.every(20).seconds.do(fun) #Problem

if __name__ == "__main__":
	main()