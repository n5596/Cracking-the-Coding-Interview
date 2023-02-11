# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum_curr = None
        carry = 0
        
        while l1 != None or l2 != None:
            
            if l1 != None and l2 != None:
                sum_val = l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                sum_val = l1.val+carry
                l1 = l1.next
            elif l2 != None:
                sum_val = l2.val+carry
                l2 = l2.next
                
            val = (sum_val)%10
            carry = sum_val//10
            
            if sum_curr == None:
                sum_head = ListNode(val)
                sum_curr = sum_head
            else:
                sum_curr.next = ListNode(val)
                sum_curr = sum_curr.next
                
        if carry != 0:
            sum_curr.next = ListNode(carry)
        return sum_head
