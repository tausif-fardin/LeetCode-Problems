from typing import Optional


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt
    return prev
