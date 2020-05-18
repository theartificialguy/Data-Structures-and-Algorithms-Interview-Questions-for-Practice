#time complexity: 0(n^3)
#space complexity: 0(1)
# def three_sum_brute_force(nums):
#     for i in range(len(nums)-2): #we stop 2 elements away cuz otherwise we cudnt compare 3 nums
#         for j in range(i+1,len(nums)-1):
#             for k in range(j+1,len(nums)):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     print([i, j, k])
#                     return True
#     return False

# print(three_sum_brute_force([-1,0,1,2,-1,-4]))

#using hashing
#time complexity: 0(n^2)
#space complexity: 0(n)
# def three_sum_hashing(nums):
#     for i in range(0,len(nums)-2):
#         s = set()
#         for j in range(i+1,len(nums)-1):
#             x = -(nums[i]+nums[j])
#             if x in s:
#                 print(x,nums[i],nums[j])
#                 return True
#             else:
#                 s.add(nums[j])
#     return False

# print(three_sum_hashing([-1,0,1,2,-1,-4]))

#using sorting
#time complexity: 0(n^2)
#space complexity: 0(n)

def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(0,len(array)-2):
        start = i+1
        end = len(array)-1
        while start<end:
            k = array[i] + array[start] + array[end]
            if k == targetSum:
                result.append([array[i], array[start], array[end]])
                start += 1
                end -= 1
            elif k < targetSum:
                start += 1
            else:
                end -= 1
    return result


threeNumberSum([-1,0,1,2,-1,-4])


