class Solution:
    def modifyQueue(self, q, k):
        return q[:k][::-1]+q[k:]