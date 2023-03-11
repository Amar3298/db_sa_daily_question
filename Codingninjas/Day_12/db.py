import sys
sys.setrecursionlimit(10**7)

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if((n%i)%(10**7)==0):
            return False
    return True
def primeNumbersTillN(N):
    res = []
    for i in range(N+1):
        if(isPrime(i)):
            res.append(i)
    return res

#   taking input using fast I/O
def takeInput() :
    n = int(input().strip())
    return n

def printAns(ans):
    for i in ans:
        print(i, end = ' ')

#   main
n = takeInput()
ans = primeNumbersTillN(n)
printAns(ans)