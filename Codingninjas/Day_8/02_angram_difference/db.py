def getMinimumAnagramDifference(str1, str2):
    # Write your code here.
    lst = list(str2)
    for i in str1:
        if(i in lst):
            lst.remove(i)
    return len(lst)