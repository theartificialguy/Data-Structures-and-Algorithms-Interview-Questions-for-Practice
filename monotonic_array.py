a = [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
b = []
c = [1]
d = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]

def monotonic(arr):

	isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1,len(arr)):
		if arr[i] > arr[i-1]:
			isNonIncreasing = False
		elif arr[i] < arr[i-1]:
			isNonDecreasing = False
	return isNonDecreasing or isNonIncreasing

ans = monotonic(d)
print(ans)
