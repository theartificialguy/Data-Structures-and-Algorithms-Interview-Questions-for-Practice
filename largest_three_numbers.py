a = [141,1,17,-7-17,-27,18,541,8,7,7]
b = [55,7,8]

def findLargest3(array):
	array.sort()
	return array[-3:] # -1 is the last index, so -3 would be 3rd last index, 
					  # so start from -3 to the end.	

result = findLargest3(b)
print(result)