'''
Given a root of the binary tree, return an array containing nodes in its right view.

The right view of a binary tree consists of nodes that are visible when the 
tree is viewed from the right side. For each level of the tree, the last node 
encountered in that level will be included in the right view.

Examples
Example 1
Input: root = [1, 2, 3, 4, 5, 6, 7]

       1
   2      3
 4   5  6   7

Expected Output: [1, 3, 7]
Justification:
The last node at level 0 is 1.
The last node at level 1 is 3.
The last node at level 2 is 7.

Example 2
Input: root = [12, 7, 1, null, 9, 10, 5, null, 3]
        12
    7       1
      9  10   5
        3
Expected Output: [12, 1, 5, 3]
Justification:
The last node at level 0 is 12.
The last node at level 1 is 1.
The last node at level 2 is 5.
The last node at level 3 is 3.

'''
from collections import deque
from queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''Time Complexity
The time complexity of the above algorithm is O(N), where N is the total number
of nodes in the tree. This is because we traverse each node once.
Space Complexity
The space complexity of the above algorithm is O(N) which is required for the queue.
Since we can have a maximum of N/2 nodes at any level
(this could happen only at the lowest level), therefore we will need O(N) space'''


class Solution:
    def traverseOwn(self, root):

        result = []  # List[int]
        if not root:
            return result
        # TODO: Write your code here
        q = deque([root])
        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if i == level - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result

    def traverse(self, root):
        result = []
        if root is None:
            return result

        queue = Queue()
        queue.put(root)
        while not queue.empty():
            levelSize = queue.qsize()
            currentNode = None
            for i in range(0, levelSize):
                currentNode = queue.get()
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.put(currentNode.left)
                if currentNode.right:
                    queue.put(currentNode.right)
            # Add last node of the current node in the result.
            result.append(currentNode.val)

        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = sol.traverse(root)
    print("Tree right view: ")
    for val in result:
        print(str(val) + " ", end='')


main()

''' Similar Problems:
1. [Left View of Binary Tree]
(https://leetcode.com/problems/binary-tree-left-side-view/)
Problem 1: Given a binary tree, return an array containing nodes 
in its left view. The left view of a binary tree is the set of nodes visible
when the tree is seen from the left side.'''
