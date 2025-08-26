'''
Given a root of the binary tree and an integer ‘S’, 
return true if the tree has a path from root-to-leaf such that the 
sum of all the node values of that path equals ‘S’. Otherwise, return false.

Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7], S = 10
       1
   2      3
 4   5  6   7
Output: true
Justification: The path 1 -> 2 -> 4 has a sum of 7 which is not equal to 10,
but the path 1 -> 3 -> 6 has a sum of 10.
Example 2:
Input: root = [12, 7, 1, null, 9, 10, 5, null, 3], S = 23
        12
    7       1
9       10     5
Output: true
Justification: The path 12 -> 1 -> 10 has a sum of 23
'''

class TreeNode:
 def __init__(self, val, left=None, right=None):
   self.val = val
   self.left = left
   self.right = right

'''
Time Complexity
The time complexity of the above algorithm is O(N), 
where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) in the worst case.
This space will be used to store the recursion stack.
The worst case will happen when the given tree is a linked list 
(i.e., every node has only one child).'''
class Solution:
  def hasPath(self, root, sum):
    # TODO: Write your code here
    if not root:
      return False
    
    if not root.left and not root.right:
      # We found a leaf node, the sum (leftover)
      if sum == root.val: 
        return True
      else:
        return False
    leftSTree = self.hasPath(root.left, sum-root.val)
    rightSTree = self.hasPath(root.right, sum - root.val)
    return leftSTree or rightSTree


def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)

  s = Solution()
  print(s.hasPath(root, 10))  # Output: True
  print(s.hasPath(root, 15))  # Output: False   

if __name__ == "__main__":
  main()