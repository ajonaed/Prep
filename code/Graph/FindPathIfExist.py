'''
Given an undirected graph, represented as a list of edges. 
Each edge is illustrated as a pair of integers [u, v], signifying that 
there's a mutual connection between node u and node v.

You are also given starting node start, and a destination node end, 
return true if a path exists between the starting node and the destination node. 
Otherwise, return false.

Example 1:
Input: n = 4, edges = [[0,1],[1,2],[2,3]], start = 0, end = 3
Output: true
Explanation: There is a path between node 0 and node 3 as follows: 0 -> 1 -> 2 -> 3

Example 2:
Input: n = 4, edges = [[0,1],[2,3]], start = 0, end = 3
Output: false
Explanation: There is no path between node 0 and node 3.

Example 3:
Input: n = 5, edges = [[0,1],[3,4]], start = 0, end = 4
Output: false

'''

'''
Time Complexity
Graph Construction: Constructing the adjacency list from the given edge list takes , 
where (E) is the number of edges. Each edge is processed once.

DFS Traversal: In the worst-case scenario, the Depth-First Search (DFS) 
can traverse all nodes and all edges once. This traversal has a time complexity of , 
where (V) is the number of vertices or nodes, and (E) is the number of edges.

Combining the above, our time complexity is dominated by the DFS traversal, 
making it O(V + E) .

Space Complexity
Graph Representation: The adjacency list requires O(V + E) space.

Visited Set/Array: The visited set (or array) will take O(V) space, as 
it needs to track each node in the graph.

Recursive Call Stack: The DFS function is recursive, and in the worst case 
(for a connected graph), it can have (V) nested calls. This would result 
in a call stack depth of (V), adding O(V) space complexity.

The dominant factor here is the graph representation and the call stack, 
so the total space complexity is O(V + E).

This makes our algorithm efficient, especially for sparse graphs 
(i.e., graphs with relatively fewer edges compared to nodes). 
The worst-case scenario is when the graph is fully connected, 
but even then, our algorithm is designed to handle it within reasonable limits.
'''
from collections import defaultdict


class Solution:
    def validPathOwn(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        # ToDo: Write Your Code Here.
        visited = [False] * n
        # build the adjacency list
        self.adjList = [[] for _ in range(n)]
        for i in edges:
            self.adjList[i[0]].append(i[1])
            self.adjList[i[1]].append(i[0])
        return True if self.dfs(start, end, visited) == 1 else False

    def dfs(self, current, end, visited):
        visited[current] = True
        if current == end:
            return True

        for i in self.adjList[current]:
            if not visited[i] and self.dfs(i, end, visited):
                return True
        return False
    
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        
        # Create graph from edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph
        
        visited = set()

        def helper(node):
            if node == end:  # Found the path
                return True
            visited.add(node)
            
            # Traverse neighbors
            for neighbor in graph[node]:
                if neighbor not in visited and helper(neighbor):
                    return True
            return False  # Path not found

        return helper(start)


def main():
    n = 5
    edges = [[0, 1],  [3, 4]]
    start = 0
    end = 4
    sol = Solution()
    print(sol.validPath(n, edges, start, end))
    print(sol.validPath(4, [[0,1],[1,2],[2,3]], 0, 3))
    print(sol.validPathOwn(n, edges, start, end))
    print(sol.validPathOwn(4, [[0,1],[1,2],[2,3]], 0, 3))


if __name__ == "__main__":
    main()
