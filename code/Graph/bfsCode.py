from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # For undirected graph

    def BFS(self, startVertex):
        visited = [False] * self.V  # To keep track of visited vertices
        q = deque()

        visited[startVertex] = True
        q.append(startVertex)

        while q:
            currentVertex = q.popleft()
            print(currentVertex, end=" ")

            # Explore adjacent vertices
            for neighbor in self.adjList[currentVertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)


if __name__ == "__main__":
    graph = Graph(5)  # Create a graph with 6 vertices

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(2, 4)

    print("Breadth-First Traversal starting from vertex 0:")
    graph.BFS(0)


'''
Time Complexity
Initialization:

The visited array is initialized to track whether a vertex has been visited. This operation is , where V is the number of vertices.
Queue Operations:

Each vertex is enqueued once when it is first discovered and dequeued once during processing. These operations together are  over the course of the BFS traversal.
Exploration of Adjacent Vertices:

The adjacency list for each vertex is iterated over to explore its neighbors.
Each edge is visited exactly once when traversing its endpoints, contributing , where E is the number of edges.
Total Time Complexity:

The traversal involves visiting all vertices and all edges:
Complexity Considerations: Traversing all vertices and edges of a graph has a 
time complexity of O(V + E), where V is the number of vertices and E is 
the number of edges.

Space Complexity
Visited Array:

The visited boolean array stores one entry per vertex to track whether it has been visited. Space Requirement: .
Queue:

In the worst case, the queue can hold all vertices in a connected component, requiring  space.
Total Space Complexity:

Overall Space Requirement: O(V) (from visited array and queue).
'''