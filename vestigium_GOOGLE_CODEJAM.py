
def diagonalSum(matrix,n):
	dsum = 0
	for i in range(n):
		dsum += matrix[i][i]
	return dsum

def isVestigiumRows(matrix,n):
	#checking for rows
	countr = 0
	nr = 0
	for i in range(n):
		cache = {}
		for j in range(n):
			if matrix[i][j] not in cache.values():
				cache[j] = matrix[i][j] #cache[key]=value
				countr += 1
			else:
				nr += 1
				break
	if countr == n**2:
		return 0
	return nr

def isVestigiumCols(matrix,n):
	#checking for cols
	from numpy import transpose
	mat = transpose(matrix)
	countc = 0
	nc = 0
	for i in range(n):
		cache = {}
		for j in range(n):
			if mat[i][j] not in cache.values():
				cache[j+100] = mat[i][j] 
				countc += 1
			else:
				nc += 1
				break
	if countc == n**2:
		return 0
	return nc


if __name__ == "__main__":

	T = int(input())

	for x in range(T):

		N = int(input())
		matrix = []
		for i in range(N):
			matrix.append(list(map(int, input().rstrip().split())))

		diagSum = diagonalSum(matrix,N)
		r = isVestigiumRows(matrix,N)
		c = isVestigiumCols(matrix,N)

		print("Case #{}: {} {} {}".format(x+1,diagSum,r,c))

