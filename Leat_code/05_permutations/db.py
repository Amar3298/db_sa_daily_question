class Solution:
    def permute(self, nums):
        res = []
        if(len(nums)==1):
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for prem in perms:
                prem.append(n)
            res.extend(perms)
            nums.append(n)
        return res

obj = Solution()
res = obj.permute([1,2,3])
print(res)