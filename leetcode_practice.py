#reverse integer
# def reverse(x):
# 	if x>2**31-1 or x <= -2**31: 
# 		return 0
# 	if x>=0:
# 		temp = str(x)
# 		return "".join(temp[::-1])
# 	else:
# 		temp1 = str(x)
# 		temp2 = temp1[1:]
# 		return "-"+"".join(temp2[::-1])

# ans = reverse(123)
# print(ans)
#--------------------------------------------------------
#integer palindrome
# def isPalindrome(x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if len(str(x))==1: return True
#         i = 0
#         j = len(str(x))-1
#         count = 0
#         while i<j:
#             if str(x)[i] == str(x)[j]:
#                 i+=1
#                 j-=1
#                 count+=1
#                 if count == len(str(x))//2:
#                     return True
#             else: return False
        
# ans = isPalindrome(1001)
# print(ans)
#--------------------------------------------------------
#roman to integer
# def romanToInt(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         vals = {
#                 'I':1,
#                 'V':5,
#                 'X':10,
#                 'L':50,
#                 'C':100,
#                 'D':500,
#                 'M':1000
#         }
#         sum1 = 0
#         if len(s)==1: return vals[s]
#         for i in range(len(s)):
#         	if i>0 and vals[s[i]]>vals[s[i-1]]:#case for negative values
#         		sum1+=vals[s[i]]-2*vals[s[i-1]]
#         	else:#only simple positive values
#         		sum1+=vals[s[i]]
#         return sum1

# ans = romanToInt("IVII")
# print(ans)
#--------------------------------------------------------
#longest common prefix
# a = ["flower","flow","flight"]

# def findCommonPrefix(str1,str2):#takes first and last strings
# 	i = 0
# 	j = 0
# 	result = ""
# 	while i<len(str1) and j<len(str2):
# 		if str1[i]==str2[j]:
# 			result+=str1[i]
# 			i+=1
# 			j+=1
# 		else: break

# 	return result

# def longest(strs):
# 	if len(strs)==0: return ""
# 	prefix = strs[0]
# 	for i in range(1,len(strs)):
# 		prefix = findCommonPrefix(prefix,strs[i])
# 	return prefix

# ans = longest(a)
# print(ans)
#--------------------------------------------------------
#valid parentheses:

# def valid(s):
# 	open_list = ["(","{","["]
# 	close_list = [")","}","]"]
# 	stack = []
# 	for char in s:
# 		if char in open_list:
# 			stack.append(char)
# 		elif char in close_list:
# 			pos = close_list.index(char)
# 			if len(stack)>0 and open_list[pos] == stack[len(stack)-1]:
# 				stack.pop()
# 			else: return False
# 	if len(stack) == 0:
# 		return True


# ans = valid("{[(]}")
# print(ans)
#--------------------------------------------------------
#remove duplicates from sorted array

# def removeDuplicates(nums):
# 	x = 1
# 	for i in range(1,len(nums)):
# 		if nums[i]!=nums[i-1]:
# 			nums[x] = nums[i]
# 			x+=1
# 	return x

# inp = [1,1,2] #op=1
# ans = removeDuplicates(inp)
# print(ans)
#--------------------------------------------------------
#--------------------------------------------------------

#LEET CODE APRIL CHALLENGE
#1 single number

# arr1 = [2,2,1] #op = 1
# arr2 = [4,2,4,2,3,5,3] #op = 5

# def single(nums):
# 	cache = []
# 	for i in range(len(nums)):
# 		if nums[i] not in cache:
# 			cache.append(nums[i])
# 		else:
# 			idx = cache.index(nums[i])
# 			cache.pop(idx)
# 	return "".join(map(str,cache))
	
# using xor in O(1) space

# def single(nums):
# 	x = 0
# 	for num in nums:
# 		x ^= num
# 	return x
#--------------------------------------------------------
#2 happy number

# def happy(n):
# 	if len(str(n)) == 1:
# 		return False
# 	digits = [int(x) for x in str(n)]

# 	while ans != 1:
# 		res = [x**2 for x in digits]
# 		ans = happy(sum(res))
# 	if ans == 1:
# 		return True
# 	return False
	

# ans1 = happy(19)
# print(ans1)
#--------------------------------------------------------
#3 maximum subarray (KADANE'S ALGORITHM)

# a = [-2,1,-3,4,-1,2,1,-5,4]

# def maxSub(nums):
# 	maxEndingHere = nums[0]
# 	maxSoFar = nums[0]
# 	for num in nums:
# 		maxEndingHere = max(num,num+maxEndingHere)
# 		maxSoFar = max(maxSoFar,maxEndingHere)
# 	return maxSoFar

# ans = maxSub(a)
# print(ans) 
#--------------------------------------------------------
# move zeros

# a = [0,1,0,3,12]

# def move(nums):
# 	emp = []
# 	cnt = 0
# 	for num in nums:
# 		if num == 0:
# 			cnt += 1
# 		else:
# 			emp.append(num)
# 	for _ in range(cnt):
# 		emp.append(0)
# 	return emp

# ans = move(a)
# print(ans)
#--------------------------------------------------------
# middle element in a linked list

# def middleNode(self, head):
	# slow_ptr = head
    # fast_ptr = head
    # while fast_ptr != None:
    #     fast_ptr = fast_ptr.next
    #     if fast_ptr == None:
    #         return slow_ptr
    #     slow_ptr = slow_ptr.next
    #     fast_ptr = fast_ptr.next
    # return slow_ptr
#--------------------------------------------------------
# backspace string compare
# s = "a##c"
# t = "#a#c"

# def backspace(S,T):
# 	return helper(S) == helper(T)

# def helper(str1):
# 	result = []
# 	for ch in str1:
# 		if ch == "#":
# 			if len(result) != 0:
# 				result.pop()
# 		else:
# 			result.append(ch)
# 	return "".join(result)


# ans = backspace(s,t)
# print(ans)
#--------------------------------------------------------
# min stack

class MinStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
    	l = len(self.stack)
    	return self.stack[l-1]

    def getMin(self):
    	return min(self.stack)












