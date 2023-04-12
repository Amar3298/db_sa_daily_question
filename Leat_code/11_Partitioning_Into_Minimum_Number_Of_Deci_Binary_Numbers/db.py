class Solution:
    def minPartitions(self, n: str) -> int:
        cur_max = 0
        for i in n:
            q = int(i)
            cur_max = max(q,cur_max)
        return cur_max