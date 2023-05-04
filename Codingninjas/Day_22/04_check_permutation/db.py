def isPermutation(string1, string2) :
    l1 = list(string1)
    l2 = list(string2)
    l1.sort()
    l2.sort()
    if(l1==l2):
        return True
    else:
        return False
print(isPermutation("abcde","baedc"))