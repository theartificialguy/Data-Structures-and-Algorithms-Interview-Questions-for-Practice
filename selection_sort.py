a = [8,5,2,9,5,6,3]

def selection(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)):
			p = j
			if arr[i]>arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
			p+=1
	return arr

sort = selection(a)
print(sort)