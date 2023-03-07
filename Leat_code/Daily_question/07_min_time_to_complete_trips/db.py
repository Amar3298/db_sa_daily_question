class Solution:
    def minimumTime(self, time, totalTrips) -> int:
        left = 1
        right = min(time) * totalTrips

        while(left < right):
            mid = (left + right)//2
            if(sum(mid//t for t in time)>= totalTrips):
                right = mid
            else:
                left = mid + 1

        return left
    
obj = Solution()
res = obj.minimumTime([1,2,3],5)
print(res)