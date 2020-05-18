a = [0,1,21,33,45,45,45,45,45,45,61,71,73]

def searchForRange(array,target):
	first = -1
	second = -1
	for i in range(len(array)):
		if array[i] == target:
			first = i
			second += 1
	return [first-second,first]


re = searchForRange(a,45)
print(re)
