def Display(A,B,C,D):
	print(A,B,C,D)
	
def main():
	# Display(10,20) //not allowerd getting errro = TypeError: Display() missing 2 required positional arguments: 'C' and 'D'
	#Display(10,20,30,40,50) #Not allowed, getting error = TypeError: Display() takes 4 positional arguments but 5 were given
	Display(12,20,30,40) #Allowed

if __name__ == "__main__":
	main()