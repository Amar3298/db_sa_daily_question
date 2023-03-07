def isPowerOfThree(n):
    # Write your code here.
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n%3!=0):
        return 0
    return isPowerOfThree(n/3)

print(isPowerOfThree(81))