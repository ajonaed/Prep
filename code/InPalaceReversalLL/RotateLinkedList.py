'''Given the head of a Singly LinkedList and a number ‘k’, 
rotate the LinkedList to the right by ‘k’ nodes.
'''
class Node:
 def __init__(self, Val, next=None):
   self.val = Val
   self.next = next

class Solution:
  def rotate(self, head, rotations):
    if head is None or head.next is None or rotations <= 0:
      return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
      last_node = last_node.next
      list_length += 1

    last_node.next = head  # connect the last node with the head to make it a circular list
    rotations %= list_length  # no need to do rotations more than the length of the list
    skip_length = list_length - rotations
    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
      last_node_of_rotated_list = last_node_of_rotated_list.next

    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
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

  print("Nodes of original LinkedList are: ", end='')
  print_list(head)
  result = sol.rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  print_list(result)


main()

'''Own Solution:'''
class SolutionOwn:
    def rotate(self, head, rotations):
        # TODO: Write your code here
        listLength = 1
        tail, prev = head, None
        while tail.next:
            tail = tail.next
            listLength += 1

        # calculate the rotation.
        rotations = rotations % listLength
        if rotations == 0:
            return head
        cur = head
        # find the pivot node, where the link will disconnected
        for i in range(listLength - rotations - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
