from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
    
obj = Solution()
res = obj.topKFrequent([1,1,1,2,2,3],2)
print(res)