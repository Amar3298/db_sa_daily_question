class Solution:
    def partitionString(self, s: str) -> int:
        list_set = []
        count = 0
        for i in s:
            if(i in list_set):
                list_set.clear()
                list_set.append(i)
                count += 1
            else:
                list_set.append(i)
        if(len(list_set)>0):
            count += 1
        return count
obj = Solution()
res = obj.partitionString("ssssss")
print(res)