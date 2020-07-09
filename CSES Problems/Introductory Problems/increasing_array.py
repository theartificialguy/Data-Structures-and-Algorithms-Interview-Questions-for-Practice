#increasing array cses-problem 4

def increasing(n, arr):
	turns = 0
	i = 1
	while i < n:
		if arr[i] >= arr[i-1]:
			i += 1
		else:
			arr[i] += 1
			turns += 1
	return turns

arr = [3,2,5,1,7]
arr2 = [1,2,1,5,3,7,2,8]
ans = increasing(len(arr2), arr2)
print(ans)