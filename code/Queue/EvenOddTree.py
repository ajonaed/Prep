'''
Given a binary tree, return true if it is an Even-Odd tree. 
Otherwise, return false.

The Even-odd tree must follow below two rules:

At every even-indexed level (starting from 0), all node values must be odd 
and arranged in strictly increasing order from left to right.

At every odd-indexed level, all node values must be even and arranged in 
strictly decreasing order from left to right.


Example 1
    Input:
           1
          / \
        10   4
        / \
       3   7
    Expected Output: true
    Justification: The tree follows both conditions for each odd and even level.
    So, it is an odd-even tree.

Example 2
    Input:

        5
       / \
      9   3
     /     \
    12      8

    Expected Output: false
    Justification: Level 1 has Odd values 9 and 3 in decreasing order, but 
    it should have even values. So, the tree is not an odd-even tree.
'''

'''
Time Complexity
The algorithm performs a level-order traversal of the binary tree, which 
means it visits each node exactly once. Therefore, the time complexity is O(N), 
where N is the number of nodes in the tree.

Space Complexity
The space complexity is determined by the maximum number of nodes at any 
level in the binary tree. In the worst case, this can be O(N) in a perfectly 
balanced tree. The space required for the queue in the level-order traversal 
is proportional to the number of nodes at the deepest level, which is O(N/2) 
in the worst case, simplifying to O(N).'''


from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTreeOwn(self, root: TreeNode) -> bool:
        # ToDo: Write Your Code Here.
        if not root:
            return True
        levelCount = 0
        q = deque([root])
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                node = q.popleft()
                temp.append(node.val)
                if levelCount % 2 == 0:
                    if node.val % 2 == 0 or (i > 0 and temp[i-1] >= temp[i]):
                        return False
                else:
                    if node.val % 2 == 1 or (i > 0 and temp[i-1] <= temp[i]):
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelCount += 1
        return True

    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True  # Check if the tree is empty

        queue = deque([root])
        level = 0  # Start with level 0

        while queue:
            size = len(queue)
            values = []  # List to store node values at current level

            for _ in range(size):
                node = queue.popleft()  # Get the next node in the queue
                values.append(node.val)  # Add its value to the list

                if node.left:
                    # Add left child to the queue if it exists
                    queue.append(node.left)
                if node.right:
                    # Add right child to the queue if it exists
                    queue.append(node.right)

            # Check values for the current level
            if level % 2 == 0:
                for i in range(len(values)):
                    if values[i] % 2 == 0 or (i > 0 and values[i] <= values[i - 1]):
                        return False  # Even level: values must be odd and strictly increasing
            else:
                for i in range(len(values)):
                    if values[i] % 2 != 0 or (i > 0 and values[i] >= values[i - 1]):
                        return False  # Odd level: values must be even and strictly decreasing
            level += 1  # Move to the next level

        return True  # If all levels satisfy the conditions, return true


# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(10)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    print(sol.isEvenOddTree(root1))  # Output: true

    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(9)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(12)
    root2.right.right = TreeNode(8)
    print(sol.isEvenOddTree(root2))  # Output: false

    # Example 3
    root3 = TreeNode(7)
    root3.left = TreeNode(10)
    root3.right = TreeNode(2)
    root3.left.left = TreeNode(12)
    root3.left.right = TreeNode(8)
    print(sol.isEvenOddTree(root3))  # Output: false
