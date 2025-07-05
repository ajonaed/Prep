'''Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
'''


''' Own Solution 

#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
    The time complexity of the above algorithm is O(n),
    where n is the number of nodes in the LinkedList.
    The space complexity is O(1) as we are not using any extra space.
  def reverse(self, head):
    result = None
    # TODO: Write your code here
    cur = head
    nextNode = None
    while cur:
      nextNode = cur.next
      # if cur == head:
      #   cur.next = None
      # else:
      #   cur.next = result
      cur.next = result
      result = cur
      cur = nextNode
    return result
'''


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    '''The time complexity of the above algorithm is O(n),
    where n is the number of nodes in the LinkedList. 
    and the space complexity is O(1) as we are not using any extra space.'''

    def reverse(self, head):
        previous, current, next = None, head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            # before we move to the next node, point previous to the current node
            previous = current
            current = next  # move on the next node
        return previous


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")  # Use temp.val to access the value
        temp = temp.next
    print()


def main():
    sol = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)
    result = sol.reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
