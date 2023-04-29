class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return (num % 9)
        
obj = Solution()
res = obj.addDigits(38)
print(res)