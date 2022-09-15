# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next
				
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
  slow = head
  fast = slow

  while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next
  
  if fast.next is None: 
    return slow
  else: 
    return slow.next  

six = ListNode(6)
five = ListNode(5, six)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

print(middleNode(one).val)