# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer_a = head
        pointer_b = head
        
        while(pointer_a and pointer_a.next):
            pointer_b = pointer_b.next
            pointer_a = pointer_a.next.next
        return pointer_b