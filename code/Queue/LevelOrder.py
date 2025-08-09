'''
Given a root node of the binary tree, perform a level-order traversal and print the value of its nodes. The traversal should start from the root and proceed level by level, from left to right.

Sample Examples
Example 1:
Input: root = [4, 5, 10, 5, 7]
Output: [4, 5, 10, 5, 7]
Justification: The binary tree's first level contains the root node 4.
The second level contains the nodes 5 and 10. 
The third level contains nodes 5 and 7.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def printLevelOrder(self, root):
        # If the tree is empty, there's nothing to print
        if root is None:
            return

        # Initialize a queue to keep track of nodes to visit
        queue = deque()
        queue.append(root) 

        while queue:
            levelSize = len(queue)  # Number of nodes at the current level

            # Iterate through all nodes at the current level
            for _ in range(levelSize):
                node = queue.popleft()  # Dequeue the next node
                print(node.val, end=" ")

                # If the left child exists, enqueue it for the next level
                if node.left is not None:
                    queue.append(node.left)

                # If the right child exists, enqueue it for the next level
                if node.right is not None:
                    queue.append(node.right)

def main():
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(5)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(7)

    print("Example 1 Output: ", end="")
    Solution().printLevelOrder(root1)  # Expected Output: 4 5 10 5 7
    print()

    # Example 2
    root2 = TreeNode(5)
    print("Example 2 Output: ", end="")
    Solution().printLevelOrder(root2)  # Expected Output: 5
    print()

if __name__ == "__main__":
    main()
