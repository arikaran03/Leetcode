# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head is None:
            return head
        pos = 1
        pointer = head
        while pointer.next is not None:
            pos += 1
            pointer = pointer.next
        
        k = k % pos
        
        dif = pos - k
        pointer2 = head
        pos2 = 1
        while pointer2.next is not None and pos2 != dif:
            pointer2 = pointer2.next
            pos2+=1
        print(pointer2.val)
        pointer.next = head
        head = pointer2.next
        pointer2.next = None
    
        return head
