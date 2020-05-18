a = [1,11,3,0,15,5,2,4,10,7,12,6]
b = [4,2,0,1,3,7,10,9]

# def largestRange(arr):
# 	arr.sort()
# 	counter = 0
# 	startIdx = 0
# 	endIdx = 0
# 	for i in range(len(arr)):
# 		if a[i]==i:
# 			endIdx = i
# 			counter+=1
# 	startIdx = endIdx - (counter-1)
# 	return [startIdx, endIdx]

# result = largestRange(b)
# print(result)

def largestRange(arr):
	arr.sort()
	counter = 0
	s = 0 
	e = 0
	for i in range(len(arr)-1):
		if isOneIncrement(arr,i,i+1):
			e = i
			counter+=1
		#e = 0
	s = e - (counter-1)
	return [s, e]

def isOneIncrement(arr,i,j):
	diff = 0
	diff = arr[j]-arr[i]
	if diff == 1:
		return True
	return False

result = largestRange(b)
print(result)