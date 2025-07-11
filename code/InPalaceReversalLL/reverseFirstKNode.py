'''
Reverse the first ‘k’ elements of a given LinkedList.

example:
    Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5

'''
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverseFirstK(self, head, k):
        if k <= 0 or head is None:
            return head

        current, previous = head, None
        count = 0

        # reverse the first 'k' nodes
        while current is not None and count < k:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            count += 1

        # connect with the rest of the list
        if head is not None:
            head.next = current

        return previous  # new head of the reversed list
def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

