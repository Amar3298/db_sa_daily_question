class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]==nums[j] and i!=j and j<i):
                    count += 1
        return count
    
obj = Solution()
res = obj.numIdenticalPairs([1,2,3,1,1,3])
print(res)