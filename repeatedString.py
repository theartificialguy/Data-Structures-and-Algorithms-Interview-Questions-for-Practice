s = "a"

def repeatedString(s,n):
    count = 0
    for i in list(s):
        if i == 'a':
            count+=1
    res = count*(n//len(s))
    for i in s[:n%len(s)]:
        if i == 'a':
            res+=1
    print(res)

repeatedString(s,1000000000)