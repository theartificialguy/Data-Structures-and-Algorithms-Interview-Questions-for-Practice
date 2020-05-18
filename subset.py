arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [4,5,10]

def sub(arr1,arr2):
    flag = 0
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                flag += 1
                break
    if flag == len(arr2):
        print("It is a subset")
    else:
        print("Not a subset")

sub(arr1,arr2)