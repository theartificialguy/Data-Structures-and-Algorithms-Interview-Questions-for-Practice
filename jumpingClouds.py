n = int(input())
arr = list(map(int,input().rstrip().split()[:n]))

def jc(arr,n):
    count = 0
    for x in arr:
        if x == 0:
            count+=1
        else:
            pass
    return count

print(jc(arr,n))