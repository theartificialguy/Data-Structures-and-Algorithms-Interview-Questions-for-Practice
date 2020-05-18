a = [1,2,3,7,10,11,7,12,6,7,16,18,19]
b = [1,2,4,7,10,11,7,12,13,14,16,18,19]

# def subsort(array):
# 	if len(array)<2:
# 		print("Size of array should be atleast 2")
# 	i = 0
# 	j = len(array)-1
# 	while i<j:
# 		if array[i]<array[j]:
# 			i+=1
# 			j-=1
# 		elif array[i]==array[j] or array[i]>array[j]:
# 			return [i,j]
# 	return [-1,-1]

# indices = subsort(a)
# print(indices) 

def subsort(array):
	i = 0
	j = i+1
	cache = {}
	while i<len(array) or j<=len(array):
		if array[i]<array[j]:
			i+=1
			j-=1
		elif array[i]>array[j]:
			endIndex = j
			if array[j] in cache:
				startIndex = cache[array[j]]
				return [startIndex, endIndex]
		cache[array[i]] = i
	return [-1,-1]

indices = subsort(a)
print(indices)
