def findCase(ch):
    if(ch.isalpha()):
        if(ch.isupper()):
            return 1
        elif(ch.islower()):
            return 0
    else:
        return -1
    
res = findCase("a")
print(res)