class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) : 
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=(arr[i]+pre[i])%K
        d={}
        ans=0;
        for i in range(n+1):
            if(pre[i] not in d):
                d[pre[i]]=i
            else:
                ans=max(ans,i-d[pre[i]])
        return ans