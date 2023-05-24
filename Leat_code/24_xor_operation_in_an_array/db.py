class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        arr = []
        for i in range(n):
            t1 = start + 2 * i 
            arr.append(t1)
        for i in arr:
            res = res ^ i 
        return res
    
obj = Solution()
res = obj.xorOperation(5,0)
print(res)