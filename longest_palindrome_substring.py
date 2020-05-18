a = "abaxyzzyxf"

def longest(string):
	maxlen = 1
	indxlow = 0
	for i in range(1,len(string)):
		#odd palindrome lengths
		start = i-1
		end = i+1
		while start>=0 and end<len(string) and string[start]==string[end]:
			if end-start+1>maxlen:
				indxlow = start
				maxlen = end-start+1
			start-=1
			end+=1
		#even palindrome lengths
		start = i-1
		end = i
		while start>=0 and end<len(string) and string[start]==string[end]:
			if end-start+1>maxlen:
				indxlow = start
				maxlen = end-start+1
			start-=1
			end+=1
	return string[indxlow:indxlow+maxlen]	

ans = longest(a)
print(ans)

