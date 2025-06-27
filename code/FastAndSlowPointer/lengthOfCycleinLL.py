'''
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
Solution: We can use the above solution to find the cycle in the LinkedList. 
Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole 
cycle with another pointer until we see the slow pointer again to find the length of the cycle.

Here is what our algorithm will look like:
'''


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def findCycleLength(self, head):
        slow = head
        fast = head
        cycleLength = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleLength = self.calculate_cycle_length(slow)

        return cycleLength

    def calculate_cycle_length(self, slow):
        current = slow
        cycleLength = 0
        while True:
            current = current.next
            cycleLength += 1
            if current == slow:
                break
        return cycleLength


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Create a cycle in the linked list
    head.next.next.next.next.next.next = head.next.next

    # Find and print the length of the cycle
    print("LinkedList cycle length: " + str(sol.findCycleLength(head)))

    # Create a longer cycle in the linked list
    head.next.next.next.next.next.next = head.next.next.next

    # Find and print the length of the longer cycle
    print("LinkedList cycle length: " + str(sol.findCycleLength(head)))


main()
