class Solution:
    def isMonotonic(self, nums):
        arr_sort = nums.copy()
        arr_sort.sort()
        rev_sort = arr_sort[::-1]
        if(nums==arr_sort):
            return True
        elif(nums==rev_sort):
            return True
        else:
            return False
obj = Solution()
res = obj.isMonotonic([1,2,2,3])
print(res)