# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            head = None
            return head
        pointer = head
        pointer2 = head
        prev = None
        while pointer and pointer.next is not None:
            

            pointer = pointer.next.next
            
            prev = pointer2
            pointer2 = pointer2.next
        prev.next = pointer2.next
        return head