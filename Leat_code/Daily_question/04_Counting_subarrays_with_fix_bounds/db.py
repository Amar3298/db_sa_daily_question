class Solution:
    def countSubarrays(self, nums, minK, maxK):
        bad = mi = ma = -1
        res = 0
        for i,n in enumerate(nums):
            if not minK<=n<=maxK:
                bad = i
            if minK == n:
                mi = i
            if maxK == n:
                ma = i
            start = min(mi,ma)

            if(start>bad):
                res += (start-bad)
        return res

obj = Solution()
res = obj.countSubarrays([1,3,5,2,7,5],1,5)
print(res)