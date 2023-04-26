class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in jewels:
            ar = stones.count(i)
            res += ar
        
        return(res)
obj = Solution()
res = obj.numJewelsInStones("aA","aAAbbbb")