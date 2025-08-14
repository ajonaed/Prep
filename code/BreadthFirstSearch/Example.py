'''
Given a root of the binary tree, return the sum of all nodes of the binary tree.
'''
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''Complexity Analysis
Time Complexity: 
The time complexity of the code is O(N) , where N is the number of nodes in 
the binary tree. This is because we visit each node exactly once during 
the BFS traversal, processing its value and checking its children.

Space Complexity: 
The space complexity is O(N) in the worst case. This happens because 
the queue will hold up to N/2 nodes at the last level of the tree in a 
complete binary tree, and we need space to store the nodes as we traverse 
the tree. Additionally, space is used for the call stack during the traversal, 
but the queue dominates the space usage.'''
class Solution:
    # Function to calculate the sum of all nodes in a binary tree using BFS
    @staticmethod
    def sumOfNodes(root):
        # If the tree is empty, return 0
        if root is None:
            return 0

        # Initialize a queue to store nodes for BFS traversal
        queue = Queue()
        queue.put(root)  # Start with the root node
        sum = 0  # Variable to store the sum of node values

        # Perform BFS traversal
        while not queue.empty():
            currentNode = queue.get()  # Remove and process the front node from the queue
            sum += currentNode.val  # Add the current node's value to the sum

            # If the left child exists, add it to the queue
            if currentNode.left:
                queue.put(currentNode.left)

            # If the right child exists, add it to the queue
            if currentNode.right:
                queue.put(currentNode.right)

        return sum

# Example usage
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print("Sum of nodes in Example 1:", Solution.sumOfNodes(root1))  # Output: 6

    # Example 2
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(6)
    print("Sum of nodes in Example 2:", Solution.sumOfNodes(root2))  # Output: 28

    # Example 3
    root3 = TreeNode(10)
    root3.left = TreeNode(5)
    root3.left.left = TreeNode(3)
    root3.left.right = TreeNode(7)
    root3.left.right.right = TreeNode(9)
    print("Sum of nodes in Example 3:", Solution.sumOfNodes(root3))  # Output: 34
