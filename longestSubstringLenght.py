# substrings = [a[i:j] for i in range(len(a)) for j in range(i+1,len(a)+1)]
# print(len(substrings))
# s = set()
# for char in substrings:
#     if char not in s:
#         s.add(char)
#     else:
#         pass
# print(len(s))

# string = "abcdefg"
# # print(list(string))
# # or 
# ['a','b','c','d','e','f']
# print(string[4:])
# splitted = [char for char in string]
# print(splitted)
# splitted = ['a','b','c','d','e','f']


# def longestSubString(s):
#     emptyList = []
#     max_len = 0
#     splitString = [c for c in s]
#     for letter in splitString:
#         if letter in emptyList:
#             emptyList = emptyList[emptyList.index(letter):]
#         else:
#             emptyList.append(letter)
#         max_len = max(max_len,len(emptyList))
#     return max_len

# a = "abcabcbb"
# a = "bbbbb"
# a = "aabaab!bb" fails at this test case
# a = "pwwkew"
# a = "aab"
# print(longestSubString(a))

#------------------
#hasmap approach
def longestSubString(s):
    hasmap = {}
    max_len, curr_max, start = 0,0,0
    for index, value in enumerate(s):
        if value in hasmap and hasmap[value] >= start:
            max_len = max(max_len,curr_max)
            curr_max = index - hasmap[value]
            start = hasmap[value]+1
        else:
            curr_max+=1
        hasmap[value] = index
    return max(max_len,curr_max)

print(longestSubString("aabaab!bb"))
