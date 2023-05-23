class Solution:
    def restoreString(self, s, indices):
        res_1 = ""
        for i in range(len(indices)):
            res_1 = res_1 + s[indices.index(i)]
        return res_1
    
obj = Solution()
res = obj.restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(res)