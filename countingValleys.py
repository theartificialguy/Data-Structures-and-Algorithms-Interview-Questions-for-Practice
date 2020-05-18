n = int(input())
arr = list(map(str,input().rstrip().split()[:n]))
#print(arr)

def cv(arr,n):
    sum_of_steps = 0 #altitude
    valleys = 0
    for val in arr:
        if val == "U":
            sum_of_steps+=1
            if sum_of_steps == 0:
                valleys+=1
        else:
            sum_of_steps-=1
    return valleys

print(cv(arr,n))
