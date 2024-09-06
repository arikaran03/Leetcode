# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        dic =  defaultdict(int)
        
        for i in nums:
            dic[i] = 1
            
        dummy = ListNode(0)
        pointer = dummy 
        
        pointer2 = head
        prev = None
        first = True
        while pointer2:
            
            val = pointer2.val 
            
            if dic[val] == 0:
                
                if first:
                    nex = pointer2.next
                    pointer.next = pointer2
                    pointer2.next = None
                    pointer = pointer2
                    pointer2 = nex
                    
                    
                    
                else:
                    pointer.next = pointer2
                    prev.next = pointer2.next
                    pointer2.next = None
                    pointer = pointer2
                    pointer2 = prev.next
            else:
                first = False
                prev = pointer2
                pointer2 = pointer2.next
        return dummy.next
            