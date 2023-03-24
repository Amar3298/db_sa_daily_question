class Solution:
    def zeroFilledSubarray(self, nums):
        i,res = 0,0
        while i< len(nums):
            count = 0
            while i< len(nums) and nums[i] == 0:
                count += 1
                i += 1
                res += count 
            
            i += 1
        return res
obj = Solution()
print(obj.zeroFilledSubarray([0,0,0,2,0,0]))