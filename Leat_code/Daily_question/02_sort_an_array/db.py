class Solution:
    def sortArray(self, nums):
        nums.sort()
        return nums
    
obj = Solution()
res = obj.sortArray([5,1,1,2,0,0])
print(res)