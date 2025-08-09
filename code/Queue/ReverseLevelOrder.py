'''
Given the root of a binary tree, return the bottom-up level order traversal 
of its nodes' values. (i.e., the lowest level comes first in left to right order.)

Example 1
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Expected Output: [[4, 5, 6, 7], [2, 3], [1]]

    Justification:
    The third level has 4, 5, 6, and 7 nodes.
    The second level has 2 and 3 nodes.
    The first level has a single node with the value 1.

Example 2
    Input: root = [12, 7, 1, null, 9, 10, 5]
    Expected Output: [[9, 10, 5], [7, 1], [12]]

    Justification:
    The third level has 9, 10, and 5 nodes.
    The second level has 7 and 1 nodes.
    The first level has a single node with the value 12.

Example 3
    Input: root = [6,5,2,null,null,1,6,3,56,3]
    Expected Output: [[3,56,3],[1,6],[5,2],[6]]

    Justification:
    The fourth level has 3, 56, and 3 nodes.
    The third level has 1, and 6 nodes.
    The second level has 5 and 2 nodes.
    The first level has a single node with the value 6.
'''
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def traverseOwn(self, root):
        stack = []
        deq = deque()
        # TODO: Write your code here
        deq.append(root)

        while deq:
            level = len(deq)
            temp = []
            for _ in range(level):
                node = deq.popleft()
                temp.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            stack.append(temp)
        res = []
        for i in range(len(stack) - 1, -1, -1):
            res.append(stack[i])
        return res

    def traverse(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                # add the node to the current level
                currentLevel.append(currentNode.val)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.appendleft(currentLevel)
        
        result = [list(sublist) for sublist in result]
        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(sol.traverse(root)))


main()
