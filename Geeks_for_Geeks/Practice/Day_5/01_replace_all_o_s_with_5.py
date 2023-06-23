def convertFive(n):
    N1 = str(n)
    res = ""
    for i in range(len(N1)):
        if(N1[i]=="0"):
            res += "5"
        else:
            res += N1[i]
    return res
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))