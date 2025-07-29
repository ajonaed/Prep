'''
Given the head node of a singly linked list, modify the list such that any 
node that has a node with a greater value to its right gets removed. 
The function should return the head of the modified list.

Examples:

Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
Output: 7 -> 4 -> 2 -> 1
Explanation: 5 and 3 are removed as they have nodes with larger values to their right.

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5
Explanation: 1, 2, 3, and 4 are removed as they have nodes with larger values
 to their right.

Input: 5 -> 4 -> 3 -> 2 -> 1
Output: 5 -> 4 -> 3 -> 2 -> 1
Explanation: None of the nodes are removed as none of them have nodes with 
larger values to their right.

'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionOwn:
    def removeNodesChatGPT(self, head):
        # TODO: Write your code here
        if not head:
            return None

        stack = []
        cur = head

        # Traverse and maintain a decreasing stack
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        # Reconstruct the linked list from the stack
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None

        return stack[0]


class Solution:
    def removeNodes(self, head):
        stack = []  # Create an empty stack to store nodes in descending order

        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()  # Remove nodes from the stack that are smaller than the current node
            if stack:
                # Update the next pointer of the top node in the stack
                stack[-1].next = cur
            stack.append(cur)  # Push the current node onto the stack
            cur = cur.next

        # Return the head of the modified list, or None if the stack is empty
        return stack[0] if stack else None


# Testing the solution
solution = Solution()

# Creating the linked list 5 -> 3 -> 7 -> 4 -> 2 -> 1
head1 = Node(5)
head1.next = Node(3)
head1.next.next = Node(7)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(2)
head1.next.next.next.next.next = Node(1)
head1 = solution.removeNodes(head1)

# Printing the modified list: 7 -> 4 -> 2 -> 1
node = head1
while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next
