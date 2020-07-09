#missing number cses problem-2

n = 5

def missing(n, nums):
	nums = sorted(nums)
	for i in range(len(nums)):
		if (i+1) != nums[i]:
			return i+1

ans = missing(7, [6,2,5,4,1,7])
print(ans)