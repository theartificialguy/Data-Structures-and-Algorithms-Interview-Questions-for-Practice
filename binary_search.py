a = [0,1,21,33,45,45,61,71,72,73]
b = [1,5,23,111]
target = 1

def binarySearch(array,target):
	start = 0
	end = len(array)-1
	found = False

	while start <= end:
		mid = (start + end)//2
		if target == array[mid]:
			found = True
			return mid
		elif target < array[mid]:
			end = mid - 1
		else: start = mid + 1

	return -1

result = binarySearch(b,target)
print(result)