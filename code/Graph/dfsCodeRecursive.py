class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacencyList = [[] for _ in range(vertices)]  # Adjacency list

    # Method to add an edge to the graph
    def addEdge(self, source, destination):
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)  # For an undirected graph

    # Method to perform DFS using recursion
    def DFS(self, startVertex):
        visited = [False] * self.vertices  # Track visited nodes
        print("DFS Traversal: ", end="")
        self.DFSRecursive(startVertex, visited)  # Start DFS from the given vertex

    def DFSRecursive(self, currentVertex, visited):
        visited[currentVertex] = True  # Mark the current node as visited
        print(currentVertex, end=" ")  # Process the current node

        # Recur for all unvisited neighbors
        for neighbor in self.adjacencyList[currentVertex]:
            if not visited[neighbor]: 
                self.DFSRecursive(neighbor, visited)


class Solution:
    @staticmethod
    def main():
        g = Graph(5)

        g.addEdge(0, 3)
        g.addEdge(0, 2)
        g.addEdge(0, 1)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.DFS(0)


Solution.main()


'''

Time Complexity

Traversal of Nodes (Vertices):
    - Each node is visited exactly once during the traversal.
    - Marking a node as visited and processing it are constant-time operations, 
      contributing O(V) for all nodes, where V is the number of vertices.
Traversal of Edges:

    - Each edge is explored exactly twice: once for each endpoint (due to the 
      undirected nature of the graph).
    - Checking the adjacency list for unvisited neighbors takes time proportional 
      to the number of edges.
    - The total time spent on edges is O(E), where E is the number of edges.
Recursive Calls:

    - The recursion explores each node and its neighbors, visiting every edge 
      exactly once.
    - The cost of recursive calls depends on the depth of recursion, which 
      corresponds to the height of the DFS tree.
Total Time Complexity:
    - Overall: O(V+E), as all vertices and edges are visited once.

Space Complexity

Visited Array:

    - The visited[] array requires O(V) space, where each element corresponds to a
      vertex in the graph.

Recursive Call Stack:

    - The depth of the recursion stack corresponds to the height of the DFS tree:
        = In the- worst case (e.g., a single long chain of nodes), 
        the depth can be equal to V, requiring O(V) stack space.
    - In a balanced graph, the height of the DFS tree is proportional to logV.
Total Space Complexity:

Overall: O(V), dominated by the recursion stack.'''