#two sum brute force
#time complexity = 0(n^2) where n = size of array
#space complexity = 0(1)
# -------------------------------------------
# def two_sum_brute_force(a,target):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j] == target:
#                 print(i,j)
#                 return True
#     return False

# print(two_sum_brute_force([-3,2,4,5,7],11))
# ---------------------------------------------
#two sum
#time complexity = 0(n)
#space complexity = 0(1)
#two pointer technique
#array shud be sorted

# def two_sum(a,target):
#     i = 0
#     j = len(a)-1
#     while i<j:
#         if a[i]+a[j] == target:
#             print(i,j)
#             return True
#         elif a[i]+a[j] < target:
#             i+=1
#         else: # a[i]+a[j] > target:
#             j-=1
#     return False

# print(two_sum([-3,2,4,5,7],11))

# #two sum using hashing
# #for unsorted ds

# USING HASHTABLES
# complexity: O(N)ST

def twoSum(array,target):
    cache = {}
    for num in array:
        hashFunc = target-num
        if hashFunc in cache:
            return [hashFunc,num]
        else:
            cache[num] = True
    return []


