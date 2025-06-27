'''
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

'''

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution1:
  def isPalindrome(self, head):
    # TODO: Write your code here
    q = head
    l2 = self.reverseList(q)
    l1 = head
    
    while l1 or l2:
      print(l1.val)
      if not l1 or not l2 or l1.val != l2.val:
        return False
      l1 = l1.next
      l2 = l2.next
    return True
  
  def reverseList(self,q):
    p = q
    nHead = None
    while p:
      cur = Node(p.val)
      cur.next = nHead
      nHead = cur
      p = p.next
    return nHead
  

class Solution2:
  def isPalindrome(self, head):
    # TODO: Write your code here
    #find the 
    slow, fast = head, head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    scn_half_head = self.reverseList(slow)
    first_head = head
    sec_head = scn_half_head
    palindrome = True
    while sec_head:
      if first_head.val != sec_head.val:
        palindrome = False
        break
      first_head = first_head.next
      sec_head = sec_head.next

    self.reverseList(scn_half_head)
    return palindrome
  

  def reverseList(self, h):
    cur = h
    nH = None
    while cur:
      p = cur.next
      cur.next = nH
      nH = cur
      cur = p
    return nH



