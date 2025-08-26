# class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
    def countPaths(self, root, S):
        # TODO: Write your code here
        return self.countPathsHelper(root, S, [])

    def countPathsHelper(self, node, s, visitedNode):
        if not node:
            return 0

        visitedNode.append(node.val)
        pathSum = 0
        pathCount = 0
        for i in range(len(visitedNode)-1, -1, -1):
            pathSum += visitedNode[i]
            if pathSum == s:
                pathCount += 1
        pathCount += self.countPathsHelper(node.left, s, visitedNode)
        pathCount += self.countPathsHelper(node.right, s, visitedNode)

        del visitedNode[-1]
        return pathCount

    '''
    Time Complexity: O(N^2) in the worst case, where N is the number of nodes
    in the tree.
    This worst case will happen when the given tree is a linked list
    (i.e., every node has only one child). As we recursive call each node twice.


    Space Complexity:
    The space complexity of the above algorithm will be O(N).
    This space will be used to store the recursion stack.
    The worst case will happen when the given tree is a linked list
    (i.e., every node has only one child). We also need O(N) space for
    storing the currentPath in the worst case.
    Overall space complexity of our algorithm is O(N).'''

    def countPathsYT(self, root, S):
        if not root:
            return 0
        # TODO: Write your code here

        def helper(node, sum):
            if not node:
                return 0
            res = 0
            if node.val == sum:
                res += 1
            res += helper(node.left, sum-node.val)
            res += helper(node.right, sum-node.val)
            return res
        return self.countPaths(root.left, S) + self.countPaths(root.right, S) + helper(root, S)

    '''
    Time Complexity:
    As we are not traversing the current path for each node, the time complexity 
    of the above algorithm will be O(N) in the worst case, where ‘N’ is the total 
    number of nodes in the tree.

    Space Complexity:
    The space complexity of the above algorithm will be O(N). 
    This space will be used to store the recursion stack, 
    as well as for the prefix sum.
    '''

    def count_paths(self, root, target_sum):
        # A map that stores the number of times a prefix sum has occurred so far.
        map = {}

        return self.count_paths_prefix_sum(root, target_sum, map, 0)

    def count_paths_prefix_sum(self, current_node, target_sum, map, current_path_sum):
        if current_node is None:
            return 0

        # The number of paths that have the required sum.
        path_count = 0

        # 'current_path_sum' is the prefix sum, i.e., sum of all node values from the root
        # to the current node.
        current_path_sum += current_node.val

        # This is the base case. If the current sum is equal to the target sum, we have found
        # a path from root to the current node having the required sum. Hence, we increment
        # the path count by 1.
        if target_sum == current_path_sum:
            path_count += 1

        # 'current_path_sum' is the path sum from root to the current node. If within this path,
        # there is a valid solution, then there must be an 'old_path_sum' such that:
        # => current_path_sum - old_path_sum = target_sum
        # => current_path_sum - target_sum = old_path_sum
        # Hence, we can search such an 'old_path_sum' in the map from the key
        # 'current_path_sum - target_sum'.
        path_count += map.get(current_path_sum - target_sum, 0)

        # This is the key step in the algorithm. We are storing the number of times the prefix sum
        # `current_path_sum` has occurred so far.
        map[current_path_sum] = map.get(current_path_sum, 0) + 1

        # Counting the number of paths from the left and right subtrees.
        path_count += self.count_paths_prefix_sum(
            current_node.left, target_sum, map, current_path_sum)
        path_count += self.count_paths_prefix_sum(
            current_node.right, target_sum, map, current_path_sum)

        # Removing the current path sum from the map for backtracking.
        # 'current_path_sum' is the prefix sum up to the current node. When we go
        # back (i.e., backtrack), then the current node is no more a part of the path, hence, we
        # should remove its prefix sum from the map.
        map[current_path_sum] = map.get(current_path_sum, 1) - 1

        return path_count


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(sol.count_paths(root, 11)))


main()
