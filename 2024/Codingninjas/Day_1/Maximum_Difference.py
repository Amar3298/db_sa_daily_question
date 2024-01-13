def maximumDifferece(n, arr):
    # Write your code here.
    min_el = min(arr)
    max_el = max(arr)
    res = max_el - min_el
    if(res%2==0):
        return 'EVEN'
    elif(res%2!=0):
        return 'ODD'