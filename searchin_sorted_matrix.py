a = [[1,4,7,12],[2,5,19,31],[3,8,24,33],[40,41,42,44]]

# def find(array,target):
# 	found = False
# 	for i in range(len(array)):
# 		for j in range(len(array[0])):
# 			if target == array[i][j]:
# 				found = True
# 				return [i, j]
# 	return [-1, -1]

# result = find(a,19)
# print(result)

def find(array,target):
	s1 = 0
	s2 = len(array[0])-1
	e1 = len(array)-1
	e2 = 0
	found = False
	while s1 <= e1 and s2 >= e2:
		if target == array[s1][s2]:
			found = True
			return [s1, s2]
		elif array[s1][s2] < target:
			s1 += 1
		else: s2 -= 1
	return [-1, -1]

result = find(a,19)
print(result)
