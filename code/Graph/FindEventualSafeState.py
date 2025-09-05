'''
You are given a directed graph with n nodes, labeled from 0 to n-1. 
This graph is described by a 2D integer array graph, where graph[i] 
is an array of nodes adjacent to node i, indicating there is a directed 
edge from node i to each of the nodes in graph[i].

A node is called a terminal node if it has no outgoing edges. A node is 
considered safe if every path starting from that node leads to a terminal 
node (or another safe node).

Return an array of all safe nodes in ascending order.

Example 1:

Input: graph = [[1,2],[2,3],[2],[],[5],[6],[]]
Expected Output: [3,4,5,6]
Explanation:
    Node 3 is a terminal node.
    Node 4 leads to node 5, which is a safe node.
    Node 5 leads to node 6, which is a terminal node.
    Node 6 is a terminal node.

Example 2:

Input: graph = [[1,2],[2,3],[5],[0],[],[],[4]]
Expected Output: [2,4,5,6]
Explanation:
    Node 2 leads to node 5, which is a terminal node.
    Node 4 is a terminal node.
    Node 5 is a terminal node.
    Node 6 leads to node 4, which is a terminal node.

Example 3:

Input: graph = [[1,2,3],[2,3],[3],[],[0,1,2]]
Expected Output: [0,1,2,3,4]
Explanation:
    Node 3 is a terminal node.
    Node 2 leads to node 3, which is a terminal node.
    Node 1 leads to node 2, which is a safe node, and node 3, which is a 
    terminal node.
    Similarly, all node leads to either a terminal or a safe node.
'''
'''
Time Complexity
The time complexity of the algorithm is O(V+E), where V is the number of vertices 
(nodes) and E is the number of edges in the graph. This is because each node and 
each edge are processed once in the depth-first search (DFS).

Space Complexity
The space complexity of the algorithm is O(V), where V is the number of vertices.
This is due to the space required to store the visited array and the 
recursion stack during the DFS.'''


class Solution:
    def eventualSafeNodesOwn(self, graph):
        result = []
        # ToDo: Write Your Code Here.
        n = len(graph)
        visited = [0] * n

        def dfs(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = 1
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visited[node] = -1
            return True
        for i in range(n):
            if dfs(i):
                result.append(i)

        return sorted(result)  # Sorting the result

    def eventualSafeNodes(self, graph):
        def dfs(node):
            if visited[node] == -1:  # If node is marked as safe
                return True
            if visited[node] == 1:  # If node is part of a cycle
                return False

            visited[node] = 1  # Mark the node as visiting
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False  # If any adjacent node is not safe

            visited[node] = -1  # Mark the node as safe
            return True

        n = len(graph)
        visited = [0] * n  # 0: unvisited, 1: visiting, -1: safe
        result = []

        for i in range(n):
            if dfs(i):
                result.append(i)

        return sorted(result)  # Sorting the result


if __name__ == "__main__":
    sol = Solution()
    print(sol.eventualSafeNodes([[1, 2], [2, 3], [2], [], [5], [6], []]))
    print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [], [], [4]]))
    print(sol.eventualSafeNodes([[1, 2, 3], [2, 3], [3], [], [0, 1, 2]]))
