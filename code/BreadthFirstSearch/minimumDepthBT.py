'''
Given a root of the binary tree, find the minimum depth of a binary tree.

The minimum depth is the number of nodes along the shortest path from the 
root node to the nearest leaf node.
A leaf is a node that does not have any children.
Example 1:
Input: 
    1
   / \
  2   3
 / \   \
4   5   6
Output: 3
Explanation: The minimum depth is 3, as there are two paths going from the root 
node to the nearest leaf node (1 -> 3 --> 6).

Example 2:
Input:
    12
   /  \
  7    1
      / \
     10  5
Output: 2
Explanation: The minimum depth is 2, as there are two paths going from the root
node to the nearest leaf node (12 -> 7).
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
    def findDepthOwn(self, root):
        minimumTreeDepth = 0
        # TODO: Write your code here
        if not root:
            return 0
        q = deque([root])

        while q:
            level = len(q)
            minimumTreeDepth += 1
            for _ in range(level):
                node = q.popleft()
                if not node.left and not node.right:
                    return minimumTreeDepth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def findDepth(self, root):
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        minimumTreeDepth = 0
        while queue:
            minimumTreeDepth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()

                # check if this is a leaf node
                if not currentNode.left and not currentNode.right:
                    return minimumTreeDepth

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(sol.findDepth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(sol.findDepth(root)))


main()
