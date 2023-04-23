class Solution:
    def leftRigthDifference(self, nums):
        res = []
        for i in range(len(nums)):
            s1 = sum(nums[:i])
            s3 = sum(nums[i+1:])
            r1 = abs(s1-s3)
            res.append(r1)
        return res
obj = Solution()
res = obj.leftRigthDifference([10,4,8,3])
print(res)