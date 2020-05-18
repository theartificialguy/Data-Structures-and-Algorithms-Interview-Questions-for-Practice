def hourglass():
    for _ in range(6):
        for _ in range(6):
            print("*",end=' ')
        print()

def hourglassArray():
    rows,cols = (6,6)
    #arr = [[0]*cols]*rows
    arr = [[0 for j in range(cols)] for i in range(rows)]
    return arr

arr = hourglassArray()

for row in arr:
    print(row)

def sumHourGLass(arr):
    tsum = -99999
    for i in range(3):
        for j in range(3):
            sum = 0
            sum += arr[i][j]
            sum += arr[i][j+1]
            sum += arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j]
            sum += arr[i+2][j+1]
            sum += arr[i+2][j+2]
            tsum = max(tsum,sum)
    return tsum

            
