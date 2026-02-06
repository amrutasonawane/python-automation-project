import gc

class Demo: 
	def __init__(self):
		print("Inside Constructor")
	def __del__(self):
		print("Inside destructor")

#allocate
obj = Demo()
obj2 = Demo()

#deallocate 
del obj #free object #no relation between __del__ and this del
del obj2

gc.collect()
print("End of application")