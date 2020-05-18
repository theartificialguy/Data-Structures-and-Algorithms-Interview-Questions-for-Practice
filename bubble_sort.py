a = [8,5,2,9,5,6,3]

def bubble_sort(array,n):
	sort = False
	for i in range(n-1): # here n-1 cuz we need to check i and "i+1"th element
		if array[i]>array[i+1]:
			array[i],array[i+1]=array[i+1],array[i]
			sort = True
	if sort == True:
		bubble_sort(array,n-1) # here n-1 cuz the last element will always
							   # be greatest so no need to iterate on it now
	else:
		return array
	return array

l = bubble_sort(a,len(a))
print(l)
