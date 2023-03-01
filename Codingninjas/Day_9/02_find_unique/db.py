def findUnique(arr, n) :
    res = 0
    for i in arr:
        res ^= i
    return res
