class Solution:
    def findDifference(self, nums1, nums2):
        res1 = []
        res3 = []
        for i in nums1:
            if(i not in nums2 and i not in res1):
                res1.append(i)
        for j in nums2:
            if(j not in nums1 and j not in res3):
                res3.append(j)
        return [res1,res3]
    
obj = Solution()
res = obj.findDifference([1,2,3],[2,4,6])
print(res)