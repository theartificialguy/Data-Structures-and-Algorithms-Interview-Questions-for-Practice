a = [1,2,3,4,5]

def leftRotate(a,d):
	for _ in range(d):
		temp = a[0] #taking the first element for every rotation
		for j in range(len(a)-1): #shifting elements to 1 posi left except first element
			a[j] = a[j+1]
		a[-1] = temp #placing the first element to last posi
	return a

arr = leftRotate(a,2)

for ele in arr:
	print(ele,end=' ')

#or

# def left(a,d):
# 	n = len(a)
# 	new = []
# 	for i in range(n):
# 		index = (i+n-d)%n
# 		new[index] = a[i]
# 	return new

# arr = left(a,4)
# print(arr)