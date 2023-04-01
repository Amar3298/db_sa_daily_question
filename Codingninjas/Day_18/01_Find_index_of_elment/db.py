n = int(input())
list1 = list(map(int,input().split()))
target = int(input())

if(target in list1):
    print(list1.index(target))
else:
    print(-1)

"""
Input
    8
    7 5 2 11 2 43 1 1
    2
Output
    2
"""
