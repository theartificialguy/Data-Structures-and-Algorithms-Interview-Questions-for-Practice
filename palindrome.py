a = "abcdba"

def isPalindrome(string):

	if len(string)==1 
		return True
		
	start = 0
	end = len(string)-1
	count = 0
	while start<end:
		if string[start]==string[end]:
			start+=1
			end-=1
			count+=1
			if count==len(string)//2:
				return True
		else:
			return False

ans = isPalindrome(a)
print(ans)
