def filterX(task,elements):
	Result = list()
	for no in elements : 
		ret = task(no)
		if(ret == True):
			Result.append(no)
	return Result

def mapX(task,elements):
	Result = list()
	for no in elements:
		Ret = task(no)
		Result.append(Ret)
	return Result

def reduceX(task,elements):
	sum = 0
	for no in elements:
		sum = task(sum,no)
	return sum