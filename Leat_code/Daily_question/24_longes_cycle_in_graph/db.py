class Solution:
    def longestCycle(self, edges):
        def find_loop(root, visited):
            """Return the first node which belongs to a loop. Otherwise, return -1"""
            if visited[root] >= 0:
                return -1
            visited[root] = root
            next = edges[root]
   
            while next != -1 and visited[next] < 0:
                visited[next] = root
                next = edges[next]

            if next != -1 and visited[next] == root:
                return next
            return -1

        def count_loop(node):
            """Count the size of a loop""" 
            next_node = edges[node]
            count = 1
            while next_node != node:
                count += 1
                next_node = edges[next_node]
            return count