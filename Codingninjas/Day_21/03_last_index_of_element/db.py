# n = int(input())
# list1 = list(map(int,input().split()))
# value = int(input())
def last_index(n,list1,value):
    if(value not in list1):
        return(-1)
    else:
        while(n!=0):
            if(list1[n-1]==value):
                return(n-1)
                break
            n -= 1

print(last_index(8,[7 ,5 ,2 ,11 ,2 ,43 ,1 ,1],2))