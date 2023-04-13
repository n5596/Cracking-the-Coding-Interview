# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s1, s2 = [], []
        
        curr1, curr2 = l1, l2
        
        while curr1 != None:
            s1.append(curr1)
            curr1 = curr1.next
        
        while curr2 != None:
            s2.append(curr2)
            curr2 = curr2.next
            
            
        curr = None
        prev = None
        carry = 0
        
        while s1 != [] or s2 != []:
            v1, v2 = 0, 0
            
            if s1 != []:
                v1 = s1.pop().val
            if s2 != []:
                v2 = s2.pop().val
                
            sum_val = v1+v2+carry
            val = sum_val%10
            carry = sum_val//10
            
            curr = ListNode(val)
            
            if prev !=  None:
                curr.next = prev
            prev = curr
            
        if carry != 0:
            curr = ListNode(carry)
            curr.next = prev
            prev = curr
        return prev
