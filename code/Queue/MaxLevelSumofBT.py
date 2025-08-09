'''
You are given the root of a binary tree. The level of its root node is 1, 
the level of its children is 2, and so on.

Return the level x where the sum of the values of all nodes is the highest. 
If there are multiple levels with the same maximum sum, return the smallest 
level number x.

Examples 1
    Input: root = [1, 20, 3, 4, 5, null, 8]
    Expected Output: 2
        Explanation:
        Level 1 has nodes: [1] with sum = 1
        Level 2 has nodes: [20, 3] with sum = 20 + 3 = 23
        Level 3 has nodes: [4, 5, 8] with sum = 4 + 5 + 8 = 17
        The maximum sum is 23 at level 2.

Example 2:
    Input: root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]
    Expected Output: 3
        Explanation:
        Level 1 has nodes: [10] with sum = 10
        Level 2 has nodes: [5, -3] with sum = 5 - 3 = 2
        Level 3 has nodes: [3, 2, 11] with sum = 3 + 2 + 11 = 16
        Level 4 has nodes: [3, -2, 1] with sum = 3 - 2 + 1 = 2
        The maximum sum is 16 at level 3.

Example 3:
    Input: root = [5, 6, 7, 8, null, null, 9, null, null, 10]
    Expected Output: 2
        Explanation:
        Level 1 has nodes: [5] with sum = 5
        Level 2 has nodes: [6, 7] with sum = 6 + 7 = 13
        Level 3 has nodes: [8, 9] with sum = 8 + 9 = 17
        Level 4 has nodes: [10] with sum = 10
        The maximum sum is 17 at level 3.
'''
'''
Time Complexity
The time complexity of the solution is O(N), where N is the number of nodes in 
the binary tree. This is because we perform a level-order traversal 
(Breadth-First Search) using a queue, which visits each node exactly once.

Space Complexity
The space complexity of the solution is O(M), where M is the maximum number 
of nodes at any level in the binary tree. This space is required for the 
queue that stores the nodes at each level during the traversal. 
In the worst case (for a complete binary tree), M can be approximately N/2, 
but it is simplified to  for asymptotic analysis.'''96



from collections import deque

# Definition for a binary tree node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSumOwn(self, root):
        if not root:
            return 0
        # ToDo: Write Your Code Here.
        maxSum = float('-inf')
        q = deque([root])
        levelCount = 0
        maxSumLevel = -1
        while q:
            level = len(q)
            curSum = 0
            levelCount += 1
            for _ in range(level):
                node = q.popleft()
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxSum < curSum:
                maxSum = curSum
                maxSumLevel = levelCount

        return maxSumLevel

    def maxLevelSum(self, root):
        if root is None:
            return 0

        queue = deque()
        queue.append(root)  # Add the root node to the queue

        maxSum = float('-inf')
        resultLevel = 1  # To keep track of the level with the maximum sum
        currentLevel = 1  # Current level counter

        while queue:
            levelSize = len(queue)
            currentSum = 0  # To calculate the sum of nodes at the current level

            for i in range(levelSize):
                node = queue.popleft()
                currentSum += node.val  # Add the node's value to the current sum

                # Add left child to the queue if it exists
                if node.left:
                    queue.append(node.left)

                # Add right child to the queue if it exists
                if node.right:
                    queue.append(node.right)

            # If the current level sum is greater than the maxSum found so far
            if currentSum > maxSum:
                maxSum = currentSum  # Update maxSum
                resultLevel = currentLevel  # Update resultLevel to the current level

            currentLevel += 1  # Increment the level counter

        return resultLevel


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    example1 = TreeNode(1)
    example1.left = TreeNode(20)
    example1.right = TreeNode(3)
    example1.left.left = TreeNode(4)
    example1.left.right = TreeNode(5)
    example1.right.right = TreeNode(8)
    print(solution.maxLevelSumOwn(example1))  # Output: 2
    print(solution.maxLevelSum(example1))  # Output: 2
