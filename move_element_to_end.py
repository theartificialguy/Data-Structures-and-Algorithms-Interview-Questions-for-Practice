a = [2,1,2,2,2,3,4,2]
num = 2

#not in-place solution
# O(factor*N)T
# O(N)S
# def move(arr,t):
# 	result = []
# 	factor = 0
# 	for num in arr:
# 		if num != t:
# 			result.append(num)
# 			factor += 1
# 	for _ in range(len(arr)-factor):
# 		result.append(t)
# 	return result

# l = move(a,num)
# print(l)

#in-place solution
# O(NLOGN+MLOGM)T
# O(1)S
def move2(arr,t):
	start = 0 
	end = len(arr)-1
	while start < end:
		while start<end and arr[end]==t:
			end-=1
		if arr[start]==t:
			arr[start],arr[end]=arr[end],arr[start]
		start+=1
	return arr

l = move2(a,num)
print(l)
