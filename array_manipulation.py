
# queries = [input([input().rstrip().split() for _ in range(3)]).rstrip().split() for _ in range(3)]
# print(queries)


nm = input().split()

n = int(nm[0]) #size of array

m = int(nm[1]) #no of operations

q = []

for _ in range(m):
    q.append(list(map(int, input().rstrip().split())))

print(q)
sum_ = 0
for i in range(0,m):
	sum_ += q[i][m]+q[q[i][0]:]+q[:q[i][1]]
print(sum_)