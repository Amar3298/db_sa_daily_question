class Solution:
    def deleteMid(self, s, sizeOfStack):
        sizeOfStack = sizeOfStack - 1 
        s.pop(sizeOfStack//2)