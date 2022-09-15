# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next
				
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  dummy = ListNode(0, head)
  
  slow, fast = dummy, dummy

  for _ in range(n):
    fast = fast.next

  while fast.next is not None:
    fast = fast.next
    slow = slow.next

  slow.next = slow.next.next    
  
  return dummy.next
  
    
six = ListNode(6)
five = ListNode(5, six)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1)

node = removeNthFromEnd(one, 1)

while node is not None:
  print(node.val)
  node = node.next
