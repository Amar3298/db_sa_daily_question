def firstMissing(arr, n):
    # Write your function here.
    arr.sort()
    i = 1
    for j in arr:
        if(i==j):
            i+=1
        if(i<j):
            return i
    return i
