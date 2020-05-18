a= [2,3,4,1,5]

def min_swap(a):
	i = 0
	j = len(a)-1
	while i < j:
		if a[i] > a[j]:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
		else:
			i += 1
			j -= 1
	return a

l = min_swap(a)
print(l)
