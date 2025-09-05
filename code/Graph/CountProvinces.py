'''
There are n cities. Some of them are connected in a network. 
If City A is directly connected to City B, and City B is directly connected 
to City C, city A is indirectly connected to City C.

If a group of cities are connected directly or indirectly, they form a province.

Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith 
city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise, 
determine the total number of provinces.

Examples
Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: There are 2 provinces: {0,1} and {2}.

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: There are 3 provinces: {0}, {1}, {2}.

'''

'''
Time Complexity:

Depth First Search (DFS): For a given node, the DFS will explore all of its
neighbors. In the worst case, we may end up visiting all nodes in the graph
starting from a single node. Hence, the DFS complexity is O(N), where O(N) is the 
number of nodes.

Overall Time Complexity: For each node, we might call DFS once 
(if that node is not visited before). Thus, the overall time complexity is 
O(N^2), with the DFS call being nested inside a loop that iterates over all 
nodes. In dense graphs where each node is connected to every other node, 
we will reach this upper bound.

Space Complexity:

Visited Array: This is an array of size (n) (the number of nodes), 
so its space requirement is O(N).

Recursive Call Stack: In the worst case, if all cities are connected in 
a linear manner (like a linked list), the maximum depth of recursive 
DFS calls will be (n). Hence, the call stack will take O(N) space.
Overall Space Complexity: The dominant space-consuming factors are the 
visited array and the recursive call stack. Hence, the space complexity is O(N).
'''


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union_set(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # If they are in the same set, do nothing.
        if rootX == rootY:
            return

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


class Solution:
    def findProvinces(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfProvinces = n

        # Iterate over each pair of nodes and union the sets if there is a connection.
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfProvinces -= 1
                    uf.union_set(i, j)

        return numberOfProvinces

    def findProvincesOwn(self, isConnected):
        # ToDo: Write Your Code Here.
        def dfs(city):
            visited.add(city)
            for j in range(n):  # J represents other cities
                if isConnected[city][j] and j not in visited:
                    dfs(j)
            return
        province = 0
        visited = set()
        n = len(isConnected)  # each represent one city
        for i in range(n):
            if i not in visited:
                province += 1
                dfs(i)
        return province


# Main method for testing
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    example1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example1))  # Expected Output: 2

    # Example 2
    example2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.findProvinces(example2))  # Expected Output: 3

    # Example 3
    example3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    print(solution.findProvinces(example3))  # Expected Output: 2
