stack = []
s = "leet**cod*e"
for i in s:
    if(len(stack)>=1 and i=="*"):
        stack.pop()
    elif(i!="*"):
        stack.append(i)

res = "".join(stack)
print(res)
