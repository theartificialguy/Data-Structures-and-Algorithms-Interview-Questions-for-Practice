# WAYS TO TAKE INPUT FROM USER
#1ST WAY
n = int(input())
# arr = []
# for _ in range(n):
#     element = int(input())
#     arr.append(element)

#2ND WAY
a = list(map(int,input().split()[:n]))
#print(a)

#algo: 
#1)we will create an empty set/list.
#2)start iterating thru array, if value present in set/list, we remove that element
#and +1 counter
#3)if value is not present in list, we append the value in set/list
#4)return count

def socksPair(n,arr):
    l = []
    count = 0
    for i in range(n):
        if arr[i] in l:
            l.remove(arr[i])
            count+=1
        else:
            l.append(arr[i])
    return count

print(socksPair(n,a))   
