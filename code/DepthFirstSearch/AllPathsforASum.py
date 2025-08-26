'''
Given a binary tree and a number ‘S’, find all paths from root-to-leaf
such that the sum of all the node values of each path equals ‘S’.
Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7], S = 10
       1
   2      3
 4   5  6   7
Output: [[1, 2, 4], [1, 3, 6]]
Justification: The paths 1 -> 2 -> 4 and 1 -> 3 -> 6 have a sum of 7
which is equal to 10.

Example 2:
Input: root = [12, 7, 1, null, 4, 10, 5], S = 23
        12
     7       1
    4    10     5
Output: [[12, 1, 10], [12, 7, 4]]
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Time Complexity
The time complexity of the above algorithm is O(N^2), where ‘N’ is the total 
number of nodes in the tree. This is due to the fact that we traverse 
each node once (which will take O(N)), and for every leaf node, 
we might have to store its path (by making a copy of the current path) 
which will take O(N).
We can calculate a tighter time complexity of O(NlogN) from the space complexity 
discussion below.

Space Complexity
If we ignore the space required for the allPaths list, the space complexity 
of the above algorithm will be O(N) in the worst case. This space will be 
used to store the recursion stack. The worst-case will happen when the given 
tree is a linked list (i.e., every node has only one child).
'''


class Solution:
    def findPathsOwn(self, root, required_sum):
        allPaths = []
        # TODO: Write your code here
        self.helper(root, required_sum, [], allPaths)

        return allPaths

    def helper(self, root, sum, curPath, allPaths):
        if not root:
            return
        curPath.append(root.val)
        if not root.left and not root.right and root.val == sum:
            allPaths.append(list(curPath))
        else:
            self.helper(root.left, sum-root.val, curPath, allPaths)
            self.helper(root.right, sum-root.val, curPath, allPaths)
        del curPath[-1]

    def findPaths(self, root, required_sum):
        allPaths = []
        self.findPaths_recursive(root, required_sum, [], allPaths)
        return allPaths

    def findPaths_recursive(self, currentNode, required_sum, currentPath, allPaths):
        if currentNode is None:
            return

        # add the current node to the path
        currentPath.append(currentNode.val)

        # if the current node is a leaf and its value is equal to required_sum, 
        # save the current path
        if currentNode.val == required_sum and currentNode.left is None \
                and currentNode.right is None:
            allPaths.append(list(currentPath))
        else:
            # traverse the left sub-tree
            self.findPaths_recursive(currentNode.left, required_sum -
                                     currentNode.val, currentPath, allPaths)
            # traverse the right sub-tree
            self.findPaths_recursive(currentNode.right, required_sum -
                                     currentNode.val, currentPath, allPaths)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currentPath[-1]


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(sol.findPathsOwn(root, required_sum)))
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(sol.findPaths(root, required_sum)))


main()


'''
Similar Problems
Problem 1: Given a binary tree, return all root-to-leaf paths.

Solution: We can follow a similar approach. We just need to remove the 
“check for the path sum.”

Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.

Solution: We need to find the path with the maximum sum. As we traverse all paths,
we can keep track of the path with the maximum sum.'''
