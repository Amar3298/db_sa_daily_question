class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        if k < arr[0]:
            return k
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2

            if(arr[mid]-(mid + 1)<k):
                l = mid + 1
            else:
                r = mid - 1

        return l+k
obj = Solution()
res = obj.findKthPositive([2,3,4,7,11],5)
print(res)