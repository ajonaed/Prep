'''
Given the root of a binary tree,
return an array containing the largest value in each row of the tree (0-indexed).

Example 1
Input: root = [1, 2, 3, 4, 5, null, 6]
Expected Output: [1, 3, 6]
Justification:
The first row contains 1. The largest value is 1.
The second row has 2 and 3, and the largest is 3.
The third row has 4, 5, and 6, and the largest is 6.

Example 2
    Input: root = [7, 4, 8, 2, 5, null, 9, null, 3]
    Expected Output: [7, 8, 9, 3]
    Image
    Justification:
    The first row contains 7, and the largest value is 7.
    The second row has 4 and 8, and the largest is 8.
    The third row has 2, 5, and 9, and the largest is 9.
    The fourth row has 3, and the largest is 3.

Example 3
    Input: root = [10, 5]
    Expected Output: [10, 5]
    Justification:
    The first row has 10, and the largest value is 10.
    The second row contains 5, and the largest is 5.
'''

from typing import List
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # Method to find the largest value in each row of the binary tree
    def largestValuesOwn(self, root: TreeNode) -> List[int]:
        result = []
        # ToDo: Write Your Code Here.
        q = deque()
        q.append(root)

        while q:
            level = len(q)
            current_max = float('-inf')
            for _ in range(level):
                node = q.popleft()
                current_max = max(node.val, current_max)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current_max)
        return result
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []

        # Return an empty list if the root is null
        if root is None:
            return result

        # Initialize a queue for level order traversal
        queue = deque([root])

        # Perform level order traversal
        while queue:
            levelSize = len(queue)
            maxVal = float('-inf')

            # Traverse all nodes at the current level
            for _ in range(levelSize):
                node = queue.popleft()

                # Find the maximum value at the current level
                maxVal = max(maxVal, node.val)

                # Add left and right children to the queue for the next level
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # Store the largest value of the current level
            result.append(maxVal)

        return result



def main():
    solution = Solution()

    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
000000000000
    output1 = solution.largestValues(root1)
    print("Example 1 Output:", output1)  # Expected Output: [1, 3, 6]

    # Example 2
    root2 = TreeNode(7)
    root2.left = TreeNode(4)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(9)
    root2.left.left.right = TreeNode(3)

    output2 = solution.largestValues(root2)
    print("Example 2 Output:", output2)  # Expected Output: [7, 8, 9, 3]

    # Example 3
    root3 = TreeNode(10)
    root3.left = TreeNode(5)

    output3 = solution.largestValues(root3)
    print("Example 3 Output:", output3)  # Expected Output: [10, 5]

if __name__ == "__main__":
    main()