class Solution:
    def sumOfNaturals(self, n):
        return (n * (n+1))%(10**9+7)//2

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
