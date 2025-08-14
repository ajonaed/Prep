'''
Given a binary tree, find its maximum depth (or height) using Tree BFS traversal.
The maximum depth is the number of nodes along the longest path from the root node.
Example 1:
Input: 
    1
   / /
  2   3
 / /   /
4   5   6
Output: 3
Explanation: The maximum depth is 3, as there are two paths going from the root
node to the leaf node (1 -> 2 -> 4 and 1 -> 3 -> 6).
Example 2:
Input:
      12
     /  /
    7    1
   / /    
  9  10    

Output: 3
Explanation: The maximum depth of the tree is 3, as there are two paths going
from the root node to the leaf node (12 -> 7 -> 9 and 12 -> 7 -> 10).

'''
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total 
number of nodes in the tree. This is due to the fact that we traverse each 
node once.

Space Complexity
The space complexity of the above algorithm will be O(N) which is required 
for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need  
O(N) space to store them in the queue.'''


class Solution:
    def find_maximum_depth(self, root):
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        maximumTreeDepth = 0
        while queue:
            maximumTreeDepth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

        return maximumTreeDepth


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(sol.find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(sol.find_maximum_depth(root)))


main()
