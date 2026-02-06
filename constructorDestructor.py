import gc

class Demo: 
	def __init__(self):
		print("Inside Constructor")
	def __del__(self):
		print("Inside destructor")

#allocate
obj = Demo()
#deallocate 
del obj #free object #no relation between __del__ and this del

gc.collect()
print("End of application")