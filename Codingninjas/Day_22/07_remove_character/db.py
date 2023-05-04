def removeAllOccurrencesOfChar(string,c):
    res = ""
    for i in string:
        if(i!=c):
            res += i
    return res
print(removeAllOccurrencesOfChar("aabccbaa","a"))