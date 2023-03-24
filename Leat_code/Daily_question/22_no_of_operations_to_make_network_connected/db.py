class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = [set() for i in range(n)]
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        return sum(dfs(node) for node in range(n)) - 1
obj = Solution()
print(obj.makeConnected(4,[[0,1],[0,2],[1,2]]))