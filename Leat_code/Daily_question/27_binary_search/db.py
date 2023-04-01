class Solution:
    def search(self, nums, target):
        if(target in nums):
            return nums.index(target)
        else:
            return -1
obj = Solution()
res = obj.search([-1,0,3,5,9,12],9)
print(res)