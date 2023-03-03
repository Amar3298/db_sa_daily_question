class Solution:
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
    
obj = Solution()
res = obj.buildArray([0,2,1,5,3,4])
print(res)