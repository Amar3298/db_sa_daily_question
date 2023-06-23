def reverse(S):
    res = []
    for i in S:
        res.insert(0,i)
    return "".join(res)

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
