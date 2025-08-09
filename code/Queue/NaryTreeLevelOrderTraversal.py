'''
Given an n-ary tree, return a list representing the level order traversal 
of the nodes' values in this tree.

The input tree is serialized in an array format using level order traversal, 
where the children of each node are grouped together and separated by a null value.

Example 1
Input: root = [1, null, 2, 3, 4, null, 5, 6]
Expected Output: [[1], [2, 3, 4], [5, 6]]
Justification: The root node 1 is at level 0. Nodes 2, 3, and 4 are 
the children of 1 and are at level 1. Nodes 5 and 6 are the children of 2, 
and at level 3.

Example 2
Input: root = [7, null, 3, 8, 5, null, 2, 9, null, 6, null, 1, 4, 10]

Expected Output: [[7], [3, 8, 5], [2, 9, 6, 1, 4, 10]]
Justification: The root node 7 is at level 0. Nodes 3, 8, and 5 are 
its children at level 1. Nodes 2, 9, 6, 1, 4, and 10 are at level 2.

Example 3
Input: root = [10, null, 15, 12, null, 20, null, 25, null, 30, 40]

Expected Output: [[10], [15, 12], [20, 25], [30, 40]]
Justification: The root node 10 is at level 0. Nodes 15 and 12 are 
its children at level 1. Node 20 and 25 are at level 2. Nodes 30, 
and 40 are at level 3.
'''


from collections import deque


class NAryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    '''
    Time Complexity
    The algorithm traverses each node in the n-ary tree exactly once.
    For each node, the algorithm processes its children, which involves 
    adding them to the queue.
    Thus, the total time complexity is O(N), where N is the total number of 
    nodes in the tree.

    Space Complexity
    The queue may store up to O(W) nodes at the widest level of the tree, 
    where W is the maximum width of the tree.
    Therefore, the space complexity is O(N) in the worst case, which occurs 
    when the tree is a balanced tree or has a large number of nodes at the 
    same level.
    '''

    def levelOrderOwn(self, root):
        result = []  # Result list to store levels
        # ToDo: Write Your Code Here.
        q = deque([root])
        while q:
            level = len(q)
            temp = []
            for _ in range(level):
                node = q.popleft()
                temp.append(node.val)
                if node.children:
                    for i in node.children:
                        q.append(i)
            result.append(temp)
        return result  # Return the level order traversal

    def levelOrder(self, root):
        result = []  # Result list to store levels
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []  # List to store current level nodes

            for _ in range(size):
                node = queue.popleft()  # Dequeue the front node
                level.append(node.val)  # Add node value to the current level
                for child in node.children:
                    # Enqueue all children of the current node
                    queue.append(child)

            result.append(level)  # Add the current level to the result
        return result  # Return the level order traversal


def main():
    sol1 = Solution()
    root = NAryNode(1, [NAryNode(2), NAryNode(3, [NAryNode(4)])])
    print(sol1.levelOrderOwn(root))  # Output: [[1], [2, 3], [4]]
    # Create test cases using the provided examples
    root1 = NAryNode(7)  # Root node with value 7
    node3 = NAryNode(3)  # NAryNode with value 3
    node8 = NAryNode(8)  # NAryNode with value 8
    node5 = NAryNode(5)  # NAryNode with value 5
    node2 = NAryNode(2)  # NAryNode with value 2
    node9 = NAryNode(9)  # NAryNode with value 9
    node6 = NAryNode(6)  # NAryNode with value 6
    node1 = NAryNode(1)  # NAryNode with value 1
    node4 = NAryNode(4)  # NAryNode with value 4
    node10 = NAryNode(10)  # NAryNode with value 10

    # Build the tree structure
    root1.children.extend([node3, node8, node5])

    node3.children.extend([node2, node9])

    node8.children.append(node6)

    node5.children.extend([node1, node4, node10])

    solution = Solution()
    # Expected output: [[7], [3, 8, 5], [2, 9, 6, 1, 4, 10]]
    print(solution.levelOrder(root1))
    print(sol1.levelOrderOwn(root1))


if __name__ == "__main__":
    main()
