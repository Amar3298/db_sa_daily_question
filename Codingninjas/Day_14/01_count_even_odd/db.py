from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def countEvenOdd(arr, n):    
    # Write your code here.
    set1 = set(arr)
    list2 = list(set1)
    res = list(map(lambda x:arr.count(x),list2))
    even = 0
    odd = 0
    for i in res:
        if(i%2==0):
            even += 1
        else:
            odd += 1
        
    return [odd,even]   

# Print answer.
def printAns(ans):

    print(ans[0], end=" ")
    print(ans[1])

# Taking inpit using fast I/O.
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n

# Main.
t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    ans = countEvenOdd(arr,n)
    printAns(ans)