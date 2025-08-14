'''
Given a binary tree, populate an array to represent the averages
of all of its levels.

Example 1:
Input: 
     1
   2   3
  4 5 6 7  
Output: [1, 2.5, 5.5]
Explanation:
The average of level 0 is 1, level 1 is (2+3)/2=2.5, and
level 2 is (4+5+6+7)/4=5.5

Example 2:
Input: 
     12
   7    1
  9 2 10  5
Output: [12, 4, 6.5]
Explanation:
The average of level 0 is 12, level 1 is (7+1)/2=4, and
level 2 is (9+2+10+5)/4=6.5
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''Time Complexity

The time complexity of the above algorithm is O(N), where N is the total number 
of nodes in the tree. This is due to the fact that we traverse each node once.

Space Complexity

The space complexity of the above algorithm will be O(N) which is required for 
the queue. Since we can have a maximum of N/2 nodes at any level 
(this could happen only at the lowest level), therefore we will need O(N) space 
to store them in the queue.
'''


class Solution:
    def findLevelAveragesOwn(self, root):
        result = []
        if not root:
            return result
        # TODO: Write your code here
        q = deque([root])
        while q:
            level = len(q)
            levelSum = 0
            for _ in range(level):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(levelSum / level)

        return result

    def findLevelAverages(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            levelSum = 0.0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                # add the node's value to the running sum
                levelSum += currentNode.val
                # insert the children of current node to the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            # append the current level's average to the result array
            result.append(levelSum / levelSize)

        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(sol.findLevelAverages(root)))


main()
