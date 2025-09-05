class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacencyList = [[] for _ in range(vertices)]  # Adjacency list

    # Method to add an edge to the graph
    def addEdge(self, source, destination):
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(
            source)  # For an undirected graph

    # Method to perform DFS using a stack
    def DFS(self, startVertex):
        visited = [False] * self.vertices  # Track visited nodes
        stack = []  # Stack for traversal

        stack.append(startVertex)  # Start with the given vertex

        while stack:
            current = stack.pop()  # Pop a vertex from the stack

            if not visited[current]:
                print(current, end=" ")  # Process the current node
                visited[current] = True  # Mark it as visited

            # Push all unvisited neighbors onto the stack
            for neighbor in self.adjacencyList[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)


class Solution:
    @staticmethod
    def main():
        g = Graph(5)

        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.DFS(0)


Solution.main()

'''
Time Complexity

Initialization:

    - The visited array is initialized, which takes O(V) time, where  is the 
    number of vertices.

Traversal Loop:

    - Each node is pushed onto and popped from the stack exactly once, 
      resulting in  operations for stack management.
    - The inner loop iterates over all neighbors of a vertex. Over the entire 
      execution of the algorithm, all edges are traversed once 
      (each edge is visited when exploring its endpoints).
        = For an undirected graph: Each edge is considered twice 
          (once for each endpoint), but this is still  where  is the number of edges.

Total Time Complexity:

The traversal loop involves O(V+E) operations:
    - O(V) for visiting each vertex.
    - O(E)for traversing all edges.

Overall Time Complexity: O(V+E)

Space Complexity

Visited Array:

    - A visited boolean array of size  is used to track whether each vertex has 
    been visited.
    Space Requirement: O(V).
Stack:

    - In the worst case, the stack may contain all vertices in the graph, 
    particularly in a graph with one long branch or a star graph.
    Space Requirement: O(V).
Overall Space Complexity:

The total space complexity is: O(V)
'''
