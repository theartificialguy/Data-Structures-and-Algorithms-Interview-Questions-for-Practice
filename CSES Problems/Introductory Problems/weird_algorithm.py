# weird algorithm cses probelm-1

n = 1000000

def weird(n):
	print(n, end=' ')
	while n!=1:
		if n%2 == 0:
			n//=2
		else:
			n = n*3+1
		print(n, end=' ')
	print()

weird(n)
