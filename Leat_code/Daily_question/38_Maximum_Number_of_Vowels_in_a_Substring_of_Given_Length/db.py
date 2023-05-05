class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = -1
        vovels = ['a','e','i','o','u']
        n = len(s)
        for i in range(n):
            c1 = 0
            ta = s[i:i+k]
            for j in ta:
                if(j in vovels):
                    c1 += 1
            res = max(c1,res)
        return res
obj = Solution()
res = obj.maxVowels("abciiidef",3)
print(res)