'''
Given a binary tree, populate an array to represent its zigzag level 
order traversal. You should populate the values of all nodes of the first
 level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
'''

from collections import deque


# class TreeNode:
#   def __init__(self, val):
#     self.val = val
#     self.left, self.right = None, None


class Solution:
    def traverse(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        leftToRight = True
        while queue:
            levelSize = len(queue)
            currentLevel = deque()
            for _ in range(levelSize):
                currentNode = queue.popleft()

                # add the node to the current level based on the traverse direction
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(list(currentLevel))
            # reverse the traversal direction
            leftToRight = not leftToRight

        return result

    def traverseOwn(self, root):
        result = []
        # TODO: Write your code here
        if root is None:
            return result
        q = deque([root])
        curLevel = 0
        while q:
            level = len(q)
            curLevel += 1
            processor = deque()
            for _ in range(level):
                node = q.popleft()
                if curLevel % 2 == 0:
                    processor.appendleft(node.val)
                else:
                    processor.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(list(processor))
        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(sol.traverse(root)))


main()
