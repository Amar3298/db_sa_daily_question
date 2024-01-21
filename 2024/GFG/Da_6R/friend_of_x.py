from typing import List


class Solution:
    def isFriend(self, n : int, x : int, y : int, arr : List[int]) -> str:
        # code here
        for i in arr:
            tmp = i+x
            if(tmp==y):
                return "yes"
        return "no"
    
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr = [int(i) for i in input().strip()]
        return arr 
    def print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = int(input())
        y = int(input())
        arr = IntArray().Input(n)
        obj = Solution()
        res = obj.isFriend(n,x,y,arr)
        print(res)