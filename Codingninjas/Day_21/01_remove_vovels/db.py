def removeVowels(inputString):
    # Write your code here.
    list1 = []
    res = []
    list1[:] = inputString
    vovels1 = ['a','e','i','o','u','A','E','I','O','U']
    for i in list1:
        if(i not in vovels1):
            res.append(i)

    return "".join(res)
print(removeVowels("Mobile"))