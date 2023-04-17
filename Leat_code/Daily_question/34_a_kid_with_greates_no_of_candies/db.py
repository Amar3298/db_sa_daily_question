class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        list1=[]
        for i in range(len(candies)):
            x=candies[i]+extraCandies
            if x>=max(candies):
                list1.append(True)
            else:
                list1.append(False)
        return list1
    
obj = Solution()
res = obj.kidsWithCandies([2,3,5,1,3],3)
print(res)