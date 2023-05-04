def removeConsecutiveDuplicates(string) :
    #Your code goes here.
    n=len(string)
    l=[]
    for i in range(n):
        if i==0 or string[i]!=string[i-1]:
            l.append(string[i])
    return ''.join(l)
res = removeConsecutiveDuplicates("aabccbaa")
print(res)