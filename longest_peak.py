a = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
b = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]

def longestPeak(array):
	
	if len(array) <= 2:
		return 0
	longestLeft = 0
	longestRight = 0
	for i in range(1,len(array)-1):
		if a[i] > a[i-1] and a[i] > a[i+1]:
			longestLeft = left(array,i)
			longestRight = right(array,i)
	return longestLeft + longestRight + 1

def left(array,i):
	peak = 0
	for x in range(i):
		if array[x] < array[x+1]:
			peak += 1
	return peak

def right(array,i):
	peak = 0
	for x in range(i,len(array)-1):
		if array[x] > array[x+1]:
			peak += 1
	return peak

ans = longestPeak([1,3,2])
print(ans)