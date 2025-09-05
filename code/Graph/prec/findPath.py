'''
Given an undirected graph, represented as a list of edges. 
Each edge is illustrated as a pair of integers [u, v], signifying that 
there's a mutual connection between node u and node v.

You are also given starting node start, and a destination node end, 
return true if a path exists between the starting node and the destination node. 
Otherwise, return false.

Examples
Example 1:
Input: n = 4, edges = [[0,1],[1,2],[2,3]], start = 0, end = 3
Output: true'''

class Solution:
    def validPath(self, n, edges, start, end):
        visited = set()
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node == end:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)

def main():
    solution = Solution()
    edges1 = [[0,1],[1,2],[2,3]]
    print(solution.validPath(4, edges1, 0, 3))  # Expected: True
    edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    print(solution.validPath(6, edges2, 0, 5))  # Expected: False  

if __name__ == "__main__":
    main()