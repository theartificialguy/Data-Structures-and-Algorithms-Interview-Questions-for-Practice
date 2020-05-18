a = "clementisacap"
b = ""

def longest(string):
	maxlen = 0
	cache = {}
	cache[string[0]] = 0
	st = 0 #starting point of current substring
	for i in range(1,len(string)):
		if string[i] not in cache:
			cache[string[i]] = i
		else:
			if cache[string[i]]>=st:
				currlen = i - st
				if maxlen<currlen:
					maxlen = currlen
				st = cache[string[i]]+1
			cache[string[i]] = i

