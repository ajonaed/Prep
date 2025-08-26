'''
Given a binary tree and a number sequence, find if the sequence is present
as a root-to-leaf path in the given tree.

Example:
Input:
    1
   / \
  0   1
 /   / \
1   6   5
Sequence: [1, 0, 6]
Output: True
Explanation: The sequence [1, 0, 6] is present as a path from root to leaf
in the tree.

Example:
Input:
    1
   / \
  0   1
 /   / \
1   6   5
Sequence: [1, 0, 7]
Output: False
Explanation: The sequence [1, 0, 7] is not present as a path from root to leaf
in the tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the 
total number of nodes in the tree. This is due to the fact that we 
traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. The worst case will 
happen when the given tree is a linked list (i.e., every node has only one child).

'''


class Solution:
    def findPathOwn(self, root, sequence):
        # TODO: Write your code here
        if not root:
            return False
        return self.helper(root, sequence, 0)

    def helper(self, node, seq, i):
        if not node:
            return False
        if not node.left and not node.right and i < len(seq) and seq[i] == node.val:
            return True
        return self.helper(node.left, seq, i+1) or self.helper(node.right, seq, i+1)

    def findPath(self, root, sequence):
        if not root:
            return len(sequence) == 0

        return self.find_path_recursive(root, sequence, 0)

    def find_path_recursive(self, currentNode, sequence, sequenceIndex):

        if currentNode is None:
            return False

        seqLen = len(sequence)
        if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
            return False

        # if the current node is a leaf, add it is the end of the sequence,
        # we have found a path!
        if currentNode.left is None and currentNode.right is None \
                and sequenceIndex == seqLen - 1:
            return True

        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
            self.find_path_recursive(
                currentNode.right, sequence, sequenceIndex + 1)


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(sol.findPath(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(sol.findPath(root, [1, 1, 6])))


main()
