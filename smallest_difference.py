arr1 = [-1,5,10,20,28,3]
arr2 = [26,134,135,15,17]

def smallestDiff(arr1,arr2):
	arr1.sort()
	arr2.sort()
	ptr1 = 0
	ptr2 = 0
	curr_diff = float("inf")
	total_diff = float("inf")
	smallest_pair = []
	
	while ptr1 < len(arr1) and ptr2 < len(arr2):
		f = arr1[ptr1]
		s = arr2[ptr2]
		
		if f < s:
			curr_diff = abs(f-s)
			ptr1 += 1 

		elif f > s:
			curr_diff = abs(f-s)
			ptr2 += 1

		else:
			return [f, s]

		if total_diff > curr_diff:
			total_diff = curr_diff
			smallest_pair = [f, s]

	return smallest_pair

l = smallestDiff(arr1,arr2)
print(l)