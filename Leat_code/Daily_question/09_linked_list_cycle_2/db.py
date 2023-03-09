class Solution:
    def detectCycle(self, head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next

        return pointer
obj = Solution()
res = obj.detectCycle([3,2,0,-4])
print(res)