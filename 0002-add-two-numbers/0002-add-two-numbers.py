# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        pointer1 = l1
        pointer2 = l2

        dummy = ListNode(0)
        pointer3 = dummy
        carry = 0
        while pointer1 and pointer2:

            a = pointer1.val
            b = pointer2.val
            c = a+b
            if carry>0:
                c = c+carry
                carry = 0
            if c<10:
                temp = ListNode(c)
                pointer3.next = temp
                pointer3 = pointer3.next
            else:
                right = c%10
                carry = c//10
                temp = ListNode(right)
                pointer3.next = temp
                pointer3 = pointer3.next

            pointer1 = pointer1.next
            pointer2 = pointer2.next

        while pointer1:
            print(carry)

            val = pointer1.val 
            c = val
            if carry>0:
                c = c+carry
                carry = 0
            if c<10:
                temp = ListNode(c)
                pointer3.next = temp
                pointer3 = pointer3.next
            else:
                right = c%10
                carry = c//10
                temp = ListNode(right)
                pointer3.next = temp
                pointer3 = pointer3.next
            pointer1 = pointer1.next

        while pointer2:
            val = pointer2.val 
            c = val
            if carry>0:
                c = c+carry
                carry = 0
            if c<10:
                temp = ListNode(c)
                pointer3.next = temp
                pointer3 = pointer3.next
            else:
                right = c%10
                carry = c//10
                temp = ListNode(right)
                pointer3.next = temp
                pointer3 = pointer3.next

            pointer2 = pointer2.next
        if carry:
            temp = ListNode(carry)
            pointer3.next = temp
        return dummy.next
