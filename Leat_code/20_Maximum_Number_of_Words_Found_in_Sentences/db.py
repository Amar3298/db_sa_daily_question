class Solution:
    def mostWordsFound(self, sentences):
        res = 0
        for i in sentences:
            list1 = i.split()
            countl = len(list1)
            res = max(countl,res)
        
        return(res)

obj = Solution()
res = obj.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(res)