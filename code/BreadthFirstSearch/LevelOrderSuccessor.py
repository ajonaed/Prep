'''
Given a root of the binary tree and an integer key, find the level order 
successor of the node containing the given key as a value in the tree.

The level order successor is the node that appears right after the given 
node in the level order traversal.


Example 1
     1
    / \
   2   3
  / \
 4   5
Input: root = [1, 2, 3, 4, 5], key = 3 
Output: 4
Explanation: The level-order traversal of the tree is [1, 2, 3, 4, 5].
The successor of 3 in this order is 4.
'''

from queue import Queue
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''
Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total 
number of nodes in the tree. This is due to the fact that we traverse each
 node once.

Space Complexity
The space complexity of the above algorithm will be O(N) which is required 
for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need O(N)
space to store them in the queue.'''


class Solution:
    def findSuccessorOwn(self, root, key):
        queue = deque()
        # TODO: Write your code here
        if root == None:
            return None
        queue.append(root)
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val == key:
                    return queue.popleft()

        return root

    def findSuccessor(self, root, key):
        if root is None:
            return None

        queue = Queue()
        queue.put(root)
        while not queue.empty():
            currentNode = queue.get()
            # insert the children of current node in the queue
            if currentNode.left:
                queue.put(currentNode.left)
            if currentNode.right:
                queue.put(currentNode.right)

            # break if we have found the key
            if currentNode.val == key:
                break

        return queue.queue[0] if not queue.empty() else None


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = sol.findSuccessor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = sol.findSuccessor(root, 9)
    if result:
        print(result.val)

    result = sol.findSuccessor(root, 12)
    if result:
        print(result.val)


main()
