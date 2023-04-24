class Solution:
    def defangIPaddr(self, address):
        ab = address.replace('.','[.]')
        return ab
obj = Solution()
res = obj.defangIPaddr("1.1.1.1")
print(res)