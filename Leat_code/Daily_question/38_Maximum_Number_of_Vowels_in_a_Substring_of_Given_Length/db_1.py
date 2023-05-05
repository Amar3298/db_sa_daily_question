class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vovels = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vovels:
                res += 1
        l = 0
        r = k - 1
        mvc = res
        while(r<len(s)-1):
            if(s[l] in vovels):
                res -= 1
            l += 1
            r += 1
            if(s[r] in vovels):
                res += 1
            mvc = max(mvc,res)
        return mvc
obj = Solution()
res = obj.maxVowels("abciiidef",3)
print(res)