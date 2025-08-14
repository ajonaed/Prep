'''
Given a root of the binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.


Example 1:
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output:
    [1 -> null]
    [2 -> 3 -> null]
    [4 -> 5 -> 6 -> 7 -> null]
    Explanation:
    The tree is traversed level by level using BFS. Each node is connected to its 
    next right node at the same level. The last node of each level points to null.
Example 2:
    Input: root = [12, 7, 1, 9, null, 10, 5]
    Output:
        [12 -> null]
        [7 -> 1 -> null]
        [9 -> 10 -> 5 -> null]
        Explanation:
        The nodes are connected to their next right sibling at the same level. 
        The last node of each level points to null.
'''


from collections import deque
from queue import Queue

'''
Time Complexity
The time complexity of the above algorithm is O(N), 
where N is the total number of nodes in the tree. This is due to the 
fact that we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N), which is required 
for the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need O(N)
space to store them in the queue.
'''
def print_level_order(root):
    nextLevelRoot = root
    while nextLevelRoot:
        current = nextLevelRoot
        nextLevelRoot = None
        while current:
            print(str(current.val) + " ", end='')
            if not nextLevelRoot:
                if current.left:
                    nextLevelRoot = current.left
                elif current.right:
                    nextLevelRoot = current.right
            current = current.next
        print()


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = self.next = None


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
            return

        queue = Queue()
        queue.put(root)
        while not queue.empty():
            previousNode = None
            levelSize = queue.qsize()
            # connect all nodes of this level
            for _ in range(levelSize):
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


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root = sol.connect(root)

    print("Level order traversal using 'next' pointer: ")
    print_level_order(root)


main()
