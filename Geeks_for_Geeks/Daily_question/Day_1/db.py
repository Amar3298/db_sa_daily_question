class Solution:
    
    def insert(self, q, k): 
        #code here
        q.append(k)
        return q
        
    def findFrequency(self, q, k):
        dict1 = {}
        for i in q:
            if(i not in dict1.keys()):
                dict1[i] = 1
            else:
                dict1[i] += 1
        if(k not in dict1.keys()):
            return 0
        else:
            return dict1[k]

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        obj = Solution()
        q = []
        n = int(input())
        arr = list(map(int, input().strip().split()));
        for k in arr:
            obj.insert(q,k)
        
        
        m = int(input())
        query = list(map(int, input().strip().split()));
        for k in query:
            f = obj.findFrequency(q,k)
            if f!=0:
                print(f)
            else:
                print(-1)

"""
Test Case 
Input:
    N = 8
    1 2 3 4 5 2 3 1
    M = 5
    1 3 2 9 10
Output:
    2
    2
    2
    -1
    -1
"""