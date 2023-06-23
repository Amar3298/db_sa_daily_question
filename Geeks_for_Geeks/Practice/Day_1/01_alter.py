class Solution:
    def subArraySum(self,arr, n, s):
        if s == 0:
            return [-1]
        sum=0
        j=0 #start index
        for i in range(n):
            sum+=arr[i]
            if sum==s:
                    return j+1, i+1  
            if sum>s:
                while sum>s:
                    sum -=arr[j]
                    j+=1
                    if sum==s:
                         return j+1, i+1
        return [-1]