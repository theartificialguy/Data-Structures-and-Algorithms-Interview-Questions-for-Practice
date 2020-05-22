a = [12,345,2,6,7896]

def even_digits(array):
	counts = 0
	for num in array:
		result = len(str(num))
		if result%2 == 0:
			counts += 1
	return counts

ans = even_digits(a)
print(ans)