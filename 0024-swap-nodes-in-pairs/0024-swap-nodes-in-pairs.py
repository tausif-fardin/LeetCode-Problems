# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # nodes to be swapped
            first_node = head
            second_node = head.next

            # swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # update head and prev for next iteration
            prev = first_node
            head = first_node.next

        return dummy.next