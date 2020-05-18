a = [7,6,4,-1,1,2]
target = 16


# O(N^4)T
# O(N)S
# def foursum(array,targetNum):
# 	window_sum = 0
# 	result = []
# 	for i in range(0,len(array)-3):
# 		for j in range(i+1,len(array)-2):
# 			for k in range(j+1,len(array)-1):
# 				for l in range(k+1,len(array)):
# 					window_sum = array[i]+array[j]+array[k]+array[l]
# 					if window_sum == targetNum:
# 						result.append([array[i],array[j],array[k],array[l]])
# 	return result					

# l = foursum(a,target)
# print(l)

#O(N^3)T
#O(N)S
def foursum(array,targetNum):
	array.sort()
	result = []
	for x in range(0,len(array)-3):
		for y in range(x+1,len(array)-2):
			i = y+1
			j = len(array)-1
			while i<j:
				if array[i]+array[j]+array[x]+array[y]==targetNum:
					result.append([array[x],array[y],array[i],array[j]])
					i+=1
					j-=1
				elif array[i]+array[j]+array[x]+array[y]<targetNum:
					i+=1
				else:
					j-=1
	return result

l = foursum(a,target)
print(l)