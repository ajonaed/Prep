'''
Given a binary tree, populate an array to represent its level-by-level 
traversal. You should populate the values of all nodes of each level from 
left to right in separate sub-arrays.
'''


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''
Time Complexity: O(N)
The time complexity is O(N) where N is the number of nodes in the binary tree.

Space Complexity: O(N)
The space complexity is O(N) as we need to store the nodes in the queue for BFS.
Since we can have a maximum of N/2 nodes at any level (this could happen only 
at the lowest level), therefore we will need O(N) space to store them in the queue.

'''


class Solution:
    def traverse(self, root):
        result = []
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

            result.append(currentLevel)

        return result

    def traverseOwn(self, root):
        result = []
        # TODO: Write your code here
        q = deque([root])
        while q:
            level = len(q)
            temp = []
            for _ in range(level):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp)
        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.traverse(root)))


main()
