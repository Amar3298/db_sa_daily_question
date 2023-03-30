def totalPrime(s,e):
    count = 0
    for n in range(s,e+1):
        flag = 0
        for i in range(2,n):
            if(n%i==0):
                flag=1
                break
        if(flag==1):
            pass
        else:
            count = count+1
    return count

s,e = map(int,input().split())
print(totalPrime(s,e))

"""
Input
    2 10
Output 
    4
"""