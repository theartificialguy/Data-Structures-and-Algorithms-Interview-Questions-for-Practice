def consec(nums):
	max_ones = 0
	current = 0
	for num in nums:
		if num == 1:
			current += 1
			if current > max_ones:
				max_ones = current
		else: current = 0
	return max_ones

a = [1,0,1,1,0,1,1,1]
ans = consec(a)
print(ans)