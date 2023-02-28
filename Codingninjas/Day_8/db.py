def nextGreaterElement(arr,n):
    nge = [0]*n
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while len(stack) and arr[i]>=stack[-1]:
            stack.pop()
        if len(stack)==0:
            nge[i] = -1
        else:
            nge[i] = stack[-1]
        stack.append(arr[i])
    return nge