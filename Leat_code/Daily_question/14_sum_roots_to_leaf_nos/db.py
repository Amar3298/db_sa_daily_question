class Solution:
    def sumNumbers(self, root) -> int:
        if root == None:
            return 0
        self.result = 0
        self.findSum(root,0)
        return self.result

    def findSum(self,root,val):
        curr = val * 10 + root.val
        if root.left == None and root.right == None:
            self.result += curr
            return

        if root.left != None:
            self.findSum(root.left  ,curr)
        if root.right != None:
            self.findSum(root.right,curr) 