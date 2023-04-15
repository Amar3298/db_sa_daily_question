class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        reverse = n[::-1]
        if(n==reverse):
            return True
        else:
            return False
obj = Solution()
res = obj.isPalindrome(121)
print(res)