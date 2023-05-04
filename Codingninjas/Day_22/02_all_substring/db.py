def printSubstrings(string) :
    for i in range(len(string)):
        for j in range(len(string)):
            a1 = string[i:j+1]
            if(len(a1)>0):
                print(a1)
res = print(printSubstrings("abc"))
print(res)