#repetitions cses problem-3

s = 'ACGGGQSAAFHGOAJSJIHISIADFNKNKJDKNDSJNFJNEJFLAKSKKMDAKSDNJNDNSDALKSDN'

def repetitions(string):
	cache = {}
	for char in string:
		if char in cache:
			cache[char] += 1
		else:
			cache[char] = 1
	
	return max(cache.values())

d = repetitions(s)
print(d)