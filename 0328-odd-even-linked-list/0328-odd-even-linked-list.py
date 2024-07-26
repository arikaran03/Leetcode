# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""if not pointer.next:
                    pre.next = dummy.next
                    return head
                    one = False
                    break"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy_pointer = dummy

        pointer = head
        pre = None
        pos = 0
        one = True
        while pointer:
            
            if pos == 1:
                
                if pointer.next is None:
                    dummy_pointer.next = pointer
                    pre.next = None
                    pointer = pointer.next
                else:
                    temp = pointer.next
                    dummy_pointer.next = pointer
                    dummy_pointer = pointer
                    pre.next = pointer.next 
                    pointer.next = None

                    pointer = temp
                    pre = pointer
                    pointer = pointer.next
                pos = 0
            else:
                pre = pointer
                pointer =pointer.next
            
            pos+=1
        
        
        pre.next = dummy.next
        return head
