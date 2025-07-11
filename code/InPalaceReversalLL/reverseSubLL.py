'''Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q’.

Example 1:
    Input: head = [1,2,3,4,5], p = 2, q = 4
    Output: [1,4,3,2,5] 
Example 2:
    Input: head = [1,2,3,4,5], p = 1, q = 5
    Output: [5,4,3,2,1]

'''

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head

        # after skipping 'p-1' nodes, current will point to 'p'th node
        current, previous = head, None
        i = 0
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        # we are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current
        next = None  # will be used to temporarily store the next node

        i = 0
        # reverse nodes between 'p' and 'q'
        while current is not None and i < q - p + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the first part
        if last_node_of_first_part is not None:
            # 'previous' is now the first node of the sub-list
            last_node_of_first_part.next = previous
        # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
        else:
            head = previous

        # connect with the last part
        last_node_of_sub_list.next = current
        return head

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)

if __name__ == "__main__":
    main()


'''Similar Questions
Problem 1: Reverse the first ‘k’ elements of a given LinkedList.

Solution: This problem can be easily converted to our parent problem; 
to reverse the first ‘k’ nodes of the list, we need to pass p=1 and q=k.

Problem 2: Given a LinkedList with ‘n’ nodes, reverse it based on its size in 
the following way:

If ‘n’ is even, reverse the list in a group of n/2 nodes.
If n is odd, keep the middle node as it is, 
reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
Solution: When ‘n’ is even we can perform the following steps:

Reverse first ‘n/2’ nodes: head = reverse(head, 1, n/2)
Reverse last ‘n/2’ nodes: head = reverse(head, n/2 + 1, n)
When ‘n’ is odd, our algorithm will look like:

head = reverse(head, 1, n/2)
head = reverse(head, n/2 + 2, n)
Please note the function call in the second step. 
We’re skipping two elements as we will be skipping the middle element.'''