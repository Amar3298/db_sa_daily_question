class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        slow, fast = head,head.next
        while(fast.next != None) and (fast.next.next != None):
            slow, fast = slow.next,fast.next.next
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

obj = Solution()
res = obj.sortedListToBST([])
print(res)