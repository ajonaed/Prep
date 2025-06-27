
# class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
    def findCycleStart(self, head):
    # TODO Write your code here
        slow, fast = head, head
        cycleLength = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleLength = self.getLength(slow)
                break
        return self.getCycleStartNode(cycleLength, head)

    def getLength(self, slow):
        cur = slow
        cycleLength = 0
        while True:
            cur = cur.next
            cycleLength += 1
            if cur == slow:
                break
        return cycleLength

    def getCycleStartNode(self, n, head):
        p, q = head, head
        while n > 0:
            q = q.next
            n -= 1
        while p != q:
            p = p.next
            q = q.next
        return p


class Solution:
    def findCycleStart(self, head):
        # TODO Write your code here using two pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



