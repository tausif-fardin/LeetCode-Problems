from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(self, head: Optional[ListNode]) -> bool:
    visited = set()

    while head != None:
        if head not in visited:
            visited.add(head)
        else:
            return True

        head = head.next

    return False
