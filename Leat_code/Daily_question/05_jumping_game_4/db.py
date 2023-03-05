import collections
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        valueToIndex = collections.defaultdict(list)

        for i,num in enumerate(arr):
            valueToIndex[num].append(i)
        queue = collections.deque([0])
        seen = set()
        seen.add(0)
        ans = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node == n-1:
                    return ans
                next = []
                if node > 0:
                    next.append(node-1)
                if node < n -1:
                    next.append(node+1)
                if arr[node] in valueToIndex:
                    next.extend(valueToIndex[arr[node]])
                    del valueToIndex[arr[node]]
                for neighbor in next:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)

            ans += 1
obj = Solution()
res = obj.minJumps([100,-23,-23,404,100,23,23,23,3,404])
print(res)