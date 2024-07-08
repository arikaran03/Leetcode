# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        left_node = dummy.next
        prev = dummy
        pointer = dummy.next
        
        check = 1
        while pointer:

            if check == k:

                cur = left_node
                
                for _ in range(k-1):

                    next_node = cur.next
                    cur.next = next_node.next
                    next_node.next = prev.next
                    prev.next = next_node

                prev = cur
                left_node = cur.next
                check=0
                pointer = cur
            
            check +=1
            pointer = pointer.next

        return dummy.next