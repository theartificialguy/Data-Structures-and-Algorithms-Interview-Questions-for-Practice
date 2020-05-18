s1 = "abcfdae"
s2 = "acdef"

#recursive approach

def lcs(string1,string2,m,n):
    if m == 0 or n == 0:
        return 0
    elif string1[m-1] == string2[n-1]:
        return 1+lcs(string1,string2,m-1,n-1)
    else:
        return max(lcs(string1,string2,m-1,n),lcs(string1,string2,m,n-1))

print(lcs(s1,s2,len(s1),len(s2)))

