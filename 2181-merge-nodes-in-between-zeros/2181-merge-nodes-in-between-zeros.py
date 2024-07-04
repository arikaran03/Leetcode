# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        new_list = None
        prev_Node = None
        pre = None
        pointer = head
        count = 0
        val = 0
        while pointer:
            
            if pointer.val == 0 and pre is None:
                count = 1
                pre = pointer
                
            elif pointer.val !=0 and pre and count!=0:
                val+= pointer.val 
            
            elif pointer.val == 0 and pre:
                
                new_node = ListNode(val)
               
                
                if new_list is None:
                    new_list = new_node
                    prev_Node = new_list
                else:
                    prev_Node.next = new_node
                    prev_Node = new_node
                    
                val = 0
                pre = pointer 
            
            pointer = pointer.next
            
        
        return new_list
                
                
            