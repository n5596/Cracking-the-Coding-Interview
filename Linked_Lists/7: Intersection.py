# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curr1, curr2 = headA, headB
        n1, n2 = 0, 0
        
        while curr1.next != None:
            curr1 = curr1.next
            n1 += 1
            
        while curr2.next != None:
            curr2 = curr2.next
            n2 += 1
            
        if curr1 != curr2:
            return None
        
        curr1, curr2 = headA, headB
        
        if n1 > n2:
            for i in range(n1-n2):
                curr1 = curr1.next
        else:
            for i in range(n2-n1):
                curr2 = curr2.next
                
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1
