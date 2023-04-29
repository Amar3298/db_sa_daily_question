class Solution:
    def runningSum(self, nums):
        res = []
        for i in range(len(nums)):
            ta = sum(nums[:i+1])
            res.append(ta)
        
        return(res)
    
obj = Solution()
res = obj.runningSum([1,2,3,4])