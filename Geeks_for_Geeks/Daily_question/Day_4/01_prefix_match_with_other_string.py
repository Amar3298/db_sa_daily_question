class Solution:
    def klengthpref(self,arr,n,k,s):
        if k>len(s):
            return 0
        filter1 = s[:k]
        res = 0
        for i in arr:
          if(i[:k]==filter1):
            res += 1 
        return res

if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
