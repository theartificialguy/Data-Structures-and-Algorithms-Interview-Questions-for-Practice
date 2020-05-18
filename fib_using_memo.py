# a dictionary can be used for caching purpose
# we store the position as key and value as value : d[6] = 20
# at key '6' we have stored the value 20
# if 6 in d: this means we are searching for key '6' in dict

cache = {}

def fib(n):
	if n in cache:
		return cache[n]
	if n == 1 or n == 2:
		value = 1
	elif n>2:
		value = fib(n-1)+fib(n-2)
	cache[n] = value
	return value

val = fib(1000)
print(val)