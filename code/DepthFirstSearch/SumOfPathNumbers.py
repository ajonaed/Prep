'''
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total 
number of nodes in the tree. This is due to the fact that we traverse each 
node once.

Space Complexity
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. The worst case will 
happen when the given tree is a linked list (i.e., every node has only one child).
'''


class Solution:
    def findSumOfPathNumbers(self, root):
        return self.find_root_to_leaf_path_numbers(root, 0)

    def find_root_to_leaf_path_numbers(self, currentNode, pathSum):
        if currentNode is None:
            return 0

        # calculate the path number of the current node
        pathSum = 10 * pathSum + currentNode.val

        # if the current node is a leaf, return the current path sum
        if currentNode.left is None and currentNode.right is None:
            return pathSum

        # traverse the left and the right sub-tree
        return self.find_root_to_leaf_path_numbers(currentNode.left, pathSum) + \
            self.find_root_to_leaf_path_numbers(currentNode.right, pathSum)

    def findSumOfPathNumbersOwn(self, root):
        # TODO: Write your code here
        if not root:
            return 0
        pathTotal = []
        self.helper(root, '', pathTotal)
        return sum(pathTotal)

    def helper(self, node, total, pathTotal):

        # Base Case 1:  node is null
        if not node:
            return
        total += str(node.val)
        # Base Case 2: node is leaf
        if not node.left and not node.right:
            pathTotal.append(int(total))
        else:
            self.helper(node.left, total, pathTotal)
            self.helper(node.right, total, pathTotal)

        total = total[:-1]


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: Own Method " +
          str(sol.findSumOfPathNumbersOwn(root)))
    print("Total Sum of Path Numbers: " + str(sol.findSumOfPathNumbers(root)))


main()
