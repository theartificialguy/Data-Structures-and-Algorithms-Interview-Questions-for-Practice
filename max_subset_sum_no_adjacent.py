a = [75,105,120,75,90,135]
# ST O(N)
def max_subset_no_adj(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	maxsums = array[:]
	maxsums[1] = max(array[0], array[1])
	for i in range(2,len(array)):
		maxsums[i] = max(maxsums[i-1], maxsums[i-2]+array[i])
	return maxsums[-1]

ans = max_subset_no_adj(a)
print(ans)

#S O(N), T O(1)
