class Solution:
    def nearlySorted(self,a,n,k):
        a.sort()
        return a

import atexit
import io
import sys
import heapq
from collections import  defaultdict

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))
