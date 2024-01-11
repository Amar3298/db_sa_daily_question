class Solution:
    def removekdigits(self,num:str,k:int) -> str:
        stack = []
        for c in num:
            # and stack means stack is not empty or we can use condition len(stack)>0
            # if top element of stack is greater that c that is next element we need to pop so we use stack[-1] > c 
            while k>0 and stack and stack[-1] > c:
                k -=1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"