import math
class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        l,r = 1,max(piles)
        res = r
        while l<=r:
            k =  (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        return res
    
obj = Solution()
res = obj.minEatingSpeed([3,6,7,11],8)
print(res)