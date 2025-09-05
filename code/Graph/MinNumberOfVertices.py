'''
Given a directed acyclic graph with n nodes labeled from 0 to n-1, 
determine the smallest number of initial nodes such that you can access 
all the nodes by traversing edges. Return these nodes.


Example 1:
    Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

    Expected Output: [0,3]
    Justification: Starting from nodes 0 and 3, you can reach all other nodes 
    in the graph. Starting from node 0, you can reach nodes 1, 2, and 5. 
    Starting from node 3, you can reach nodes 4 and 2 (and by extension 5).

Example 2:
    Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4]]
    Expected Output: [0,2,3]
    Justification: Starting from nodes 0, 2, and 3, you can reach all other nodes
    in the graph. Each of these nodes can reach node 1, which in turn can 
    reach node 4.


Step-by-Step ALgorithm
Initialization:

Create a boolean array hasIncomingEdge of size n initialized to false. 
This array tracks whether a node has any incoming edges.

Mark Nodes with Incoming Edges:

For each edge in the edges list, set hasIncomingEdge[edge[1]] = true to 
indicate that the destination node of the edge has an incoming edge.
Identify Nodes without Incoming Edges:

Initialize an empty list result to store nodes without incoming edges.
Iterate through all nodes from 0 to n-1:
If hasIncomingEdge[i] == false, add node i to the result list.
Return the Result:

Return the result list as the smallest set of vertices from which all other 
nodes are reachable.
'''
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set to store nodes with incoming edges
        nodes_with_incoming = set()
        
        # Populate the set
        for _, to_node in edges:
            nodes_with_incoming.add(to_node)
        
        # Return nodes without incoming edges
        return [i for i in range(n) if i not in nodes_with_incoming]

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    edges1 = [[0,1], [0,2], [2,5], [3,4], [4,2]]
    print(solution.findSmallestSetOfVertices(6, edges1))  # Expected: [0, 3]
    
    edges2 = [[0,1], [3,1], [1,2]]
    print(solution.findSmallestSetOfVertices(4, edges2))  # Expected: [0, 3]
    
    edges3 = [[2,0], [3,2]]
    print(solution.findSmallestSetOfVertices(4, edges3))  # Expected: [1, 3]

'''
Time Complexity:

1. Mark Nodes with Incoming Edges
The first for loop iterates over all edges in the graph:
Each edge updates the hasIncomingEdge array in constant time O(1).
If the number of edges is denoted by E, this operation takes O(E) time.

2. Identify Nodes Without Incoming Edges
The second for loop iterates over all vertices in the graph:
Checking the hasIncomingEdge array for each node takes constant time .
If the number of vertices is denoted by V, this operation takes O(V) time.

3. Overall Time Complexity: O(V + E)

Space Complexity:
1. Boolean Array (hasIncomingEdge)
The hasIncomingEdge array has a size equal to the number of vertices, n.
Space Requirement: O(V).

2. Result List
The result list stores nodes without incoming edges.
In the worst case (e.g., a graph with no incoming edges), all vertices will be 
added to the list.

Space Requirement: O(V).

4. Overall Space Complexity
The total space required is:  O(V)

'''