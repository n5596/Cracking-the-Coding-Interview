# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        
        for i in range(n):
            fast = fast.next
            
        if fast == None: # head is the nth node so skip it
            return head.next
            
        while fast.next != None:
            slow = slow.next
            fast = fast.next
            

        slow.next = slow.next.next # skip the nth node
        return head
