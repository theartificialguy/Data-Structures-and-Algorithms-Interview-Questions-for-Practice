a = [1,9,-1,-2,7,3,-1,9]
b = [3,2,6,-1,4,5,-1,2]
k = 3

def bruteForce(a,k):
    tsum = 0
    for i in range(0,(len(a)-k)+1):
        ksum = 0
        ksum += a[i]+a[i+1]+a[i+2]
        # for j in range(i,i+k):
        #     ksum += a[j]
        #print(ksum)
        tsum = max(tsum,ksum)
    return tsum

# def slidingWindow(a,k):
#     tsum = 0
#     ksum = 0
#     for i in range(0,k):
#         ksum += a[i]
#     for x in range(k,len(a)):
#         tsum = max(tsum,ksum)
#         ksum += a[x] - a[x-k]
#         tsum = max(tsum,ksum)
#     return tsum

# print(slidingWindow(a,3))

print(bruteForce(a,3))