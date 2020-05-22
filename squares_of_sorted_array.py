a = [-7,-3,2,3,11]
b = [-4,-1,0,3,10]

def squares(nums):
	for i in range(len(nums)):
		nums[i] = nums[i]*nums[i]
	return sorted(nums)

ans = squares(b)
print(ans)