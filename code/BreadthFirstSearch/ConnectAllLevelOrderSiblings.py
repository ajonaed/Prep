'''
Given a root of the binary tree, connect each node with its level order successor. 
The last node of each level should point to the first node of the next level.


Example 1
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
    Explanation: The tree is traversed level by level using BFS. Each node is 
    connected to its next node in level order traversal, including connections 
    between levels. The last node (7) points to null.

xample 2
    Input: root = [12, 7, 1, 9, null, 10, 5]
    Output: 12 -> 7 -> 1 -> 9 -> 10 -> 5 -> null
    Explanation: Each node is connected to its next node in level order traversal. 
    The last node (5) points to null,
    completing the connection of all level order siblings.
'''

from queue import Queue
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

'''
Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total 
number of nodes in the tree. This is due to the fact that we traverse each 
node once.

Space Complexity
The space complexity of the above algorithm will be O(N) which is required 
for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need  O(N) 
space to store them in the queue.
'''

class Solution:
    def connectOwn(self, root):
        # TODO: Write your code here
        q = deque()
        q.append(root)
        prev = None
        while q:
            level = len(q)

            for i in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if prev:
                    prev.next = node
                prev = node
        return root

    def connect(self, root):
        if root is None:
            return root

        queue = Queue()
        queue.put(root)
        currentNode, previousNode = None, None
        while not queue.empty():
            currentNode = queue.get()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode

            # insert the children of current node in the queue
            if currentNode.left:
                queue.put(currentNode.left)
            if currentNode.right:
                queue.put(currentNode.right)
        return root


def print_tree(node):
    print("Traversal using 'next' pointer: ", end='')
    current = node
    while current:
        print(str(current.val) + " ", end='')
        current = current.next
    print()


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sol.connect(root)
    print_tree(root)


main()
