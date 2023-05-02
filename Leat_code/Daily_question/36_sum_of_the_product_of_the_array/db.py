class Solution:
    def arraySign(self, nums):
        rest = 1
        for i in nums:
            rest *= i
        if(rest==0):
            return 0
        elif(rest>0):
            return 1
        elif(rest<0):
            return -1
        
obj = Solution()
res = obj.arraySign([-1,-2,-3,-4,3,2,1])
print(res)