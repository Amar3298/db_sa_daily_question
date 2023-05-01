class Solution:
    def average(self, salary):
        salary.sort()
        sum1 = sum(salary[1:-1])
        return sum1/len(salary[1:-1])
obj = Solution()
res = obj.average([4000,3000,1000,2000])
print(res)