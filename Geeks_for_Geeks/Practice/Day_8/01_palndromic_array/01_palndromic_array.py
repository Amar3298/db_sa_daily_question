def check_p(n):
    rv = 0
    ab = n
    while(n!=0):
        tem = n%10
        rv = rv * 10 + tem 
        n = n//10
    if(rv==ab):
        return True 
    else:
        return False
def PalinArray(arr ,n):
    for i in arr:
      if(check_p(i)==False):
        return False
    return True

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)