class Solution:
    def shuffle(self, nums, n):
        a1 = nums[:n]
        a2 = nums[n:]
        n1 = len(a1)
        res = []
        for i in range(n1):
            res.append(a1[i])
            res.append(a2[i])
        return res
    
obj = Solution()
res = obj.shuffle([2,5,1,3,4,7],3)