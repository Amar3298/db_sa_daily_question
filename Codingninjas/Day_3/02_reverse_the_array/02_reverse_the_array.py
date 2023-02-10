def reverseArray(arr, m):
    # Write your code here.
    left_part = arr[:m+1]
    right_part = arr[m+1:]
    rp = right_part[::-1]
    res = left_part + rp
    return res
