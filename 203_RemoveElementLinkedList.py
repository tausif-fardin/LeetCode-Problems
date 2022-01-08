# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            temp = curr.next
            curr.next = curr.next.next
            del temp
        else:
            curr = curr.next
    return dummy.next
