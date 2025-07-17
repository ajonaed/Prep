'''
Given the head of a LinkedList and a number ‘k’, 
reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, 
reverse it too.
Example:
    Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5
Example 2:
    Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5
'''

'''# Time Complexity: O(N)
# Space Complexity: O(1)'''


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, k):
        # TODO: Write your code here
        if k <= 1 or head is None:
            return head

        cur, prev = head, None

        while True:

            i = 0
            lastNodeOfPrevPart = prev
            lastNodeOfCurSubList = cur
            nextNode = None
            while cur and i < k:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
                i += 1

            if lastNodeOfPrevPart:
                lastNodeOfPrevPart.next = prev
            else:
                head = prev
            lastNodeOfCurSubList.next = cur

            if cur is None:
                break
            prev = lastNodeOfCurSubList

        return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)

    result = sol.reverse(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)


main()


'''

#class Node:
#  def __init__(self, val, next=None):
#    self.val = val
#    self.next = next

class Solution:
  def reverse(self, head, k):
    if k <= 1 or head is None:
      return head

    current, previous = head, None
    while True:
      last_node_of_previous_part = previous
      # after reversing the LinkedList 'current' will become the last node of the sub-list
      last_node_of_sub_list = current
      next = None  # will be used to temporarily store the next node
      i = 0
      while current is not None and i < k:  # reverse 'k' nodes
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

      # connect with the previous part
      if last_node_of_previous_part is not None:
        last_node_of_previous_part.next = previous
      else:
        head = previous

      # connect with the next part
      last_node_of_sub_list.next = current

      if current is None:
        break
       
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
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  print_list(head)
  
  result = sol.reverse(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  print_list(result)


main()
'''
