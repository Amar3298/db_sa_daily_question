arr = [6,1,2,8,3,4,7,10,5]
n = 10

nth_no = (n*(n+1))/2
res = int(abs(sum(arr)-nth_no))
print(res)

class Solution:
    def MissingNumber(self,array,n):
        # code here
        nth_no = (n*(n+1))/2
        res = abs(sum(array)-nth_no)
        return int(res)

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
