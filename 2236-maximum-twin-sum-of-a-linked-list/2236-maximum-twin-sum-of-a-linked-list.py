# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        n = 1
        pointer = head
        dic = defaultdict(int)
        dic2 = defaultdict(int)

        while pointer:
            n +=1
            pointer = pointer.next

        max_val = 0
        pointer2 = head
        pos = 1
        while pointer2:
            if dic2[pos] !=0:
                val = pointer2.val + dic[dic2[pos]] 
                max_val = max(max_val,val)
            temp = (n-pos)
            dic[pos] = pointer2.val
            dic2[temp] = pos
            
            

            pos +=1 
            pointer2 = pointer2.next
        return max_val