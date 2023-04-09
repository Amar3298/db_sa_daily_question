class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        res = 0
        for i in operations:
            if i == "--X" or i == "X--":
                res -= 1
            else:
                res += 1
        return res
    
obj = Solution()
res = obj.finalValueAfterOperations(["--X","X++","X++"])
print(res)