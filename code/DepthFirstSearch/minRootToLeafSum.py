'''
Given the root of a binary tree, explore all possible root-to-leaf paths, 
compute the sum of values along each path, and return the minimum sum.

A leaf node is a node with no children.

Example 1:
Input: root = [10, 5, 15, null, null, 7, 20]
         10
        /  \
      5    15
            /  \
          7    20
Output: 15
Explanation: The path with the minimum sum is 10 -> 5, which equals 15.

Example 2:
Input: root = [-1, 2, 3, 4, 5, 1]
         -1
        /  \
       2    3
      / \   /
    4    5 1
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''Time Complexity
The time complexity of the above algorithm is O(N), where N is the total number
of nodes in the tree. This is because we traverse each node once.
Space Complexity
The space complexity of the above algorithm is O(H), where H is the 
height of the tree. 

'''

class Solution:
    # Main function to return the minimum root to leaf sum
    def minRootToLeafSum(self, root):
        # Base case: if the tree is empty, return a large value since we are finding the minimum sum
        if root is None:
            return float('inf')

        # Base case: if we reached a leaf node, return its value
        if root.left is None and root.right is None:
            return root.val

        # Recursive case: compute the minimum sum for left and right subtrees
        leftSum = self.minRootToLeafSum(root.left)
        rightSum = self.minRootToLeafSum(root.right)

        # Return the minimum of the two sums, adding the current node's value
        return root.val + min(leftSum, rightSum)

# Example usage
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(20)

root2 = TreeNode(-1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(1)

root3 = TreeNode(8)
root3.left = TreeNode(40)
root3.right = TreeNode(12)
root3.right.left = TreeNode(10)
root3.right.right = TreeNode(18)
root3.right.left.left = TreeNode(2)

solution = Solution()

print("Minimum Root to Leaf Path Sum (Example 1):", solution.minRootToLeafSum(root1)) # Output: 15
print("Minimum Root to Leaf Path Sum (Example 2):", solution.minRootToLeafSum(root2)) # Output: 3
print("Minimum Root to Leaf Path Sum (Example 3):", solution.minRootToLeafSum(root3)) # Output: 32
