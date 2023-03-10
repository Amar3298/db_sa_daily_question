import random
class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        res = 0
        x = 1

        while curr:
            if random.random() < (1/x):
                res = curr.val
            x += 1
            curr = curr.next
        return res

obj = Solution([1,2,3])
res = obj.getRandom()
print(res)