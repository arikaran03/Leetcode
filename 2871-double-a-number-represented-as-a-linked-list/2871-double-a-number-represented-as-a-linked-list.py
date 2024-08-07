# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        one = False
        if head.val >=5:
            one = True
            head.val = (head.val*2) %10

            pre = head
            pointer = head.next
        else:
            pre = None
            pointer = head

        while pointer:
            
            if (pointer.val*2) > 9:
                
                val = pointer.val*2
                
                pointer.val = val % 10
                
                pre.val += val//10

                
                pre = pre.next
                pointer = pointer.next
            else:
                pointer.val = pointer.val *2

                pre = pointer
                pointer = pointer.next
            
        if one:
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        return head